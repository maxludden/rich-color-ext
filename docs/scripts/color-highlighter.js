function isColorToken(token) {
  const hexPattern = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i;
  return hexPattern.test(token) || CSS.supports?.("color", token);
}

function getLuminance(r, g, b) {
  // Convert RGB to relative luminance using sRGB formula
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function getContrastRatio(color1, color2) {
  const l1 = getLuminance(color1.r, color1.g, color1.b);
  const l2 = getLuminance(color2.r, color2.g, color2.b);
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}

function parseColor(colorString) {
  // Create a temporary element to parse the color
  const temp = document.createElement('div');
  temp.style.color = colorString;
  document.body.appendChild(temp);
  const computed = getComputedStyle(temp).color;
  document.body.removeChild(temp);

  // Extract RGB values from computed color
  const match = computed.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
  if (match) {
    return { r: parseInt(match[1]), g: parseInt(match[2]), b: parseInt(match[3]) };
  }
  return null;
}

function getBackgroundColor(element) {
  // Walk up the DOM tree to find the first non-transparent background
  let el = element;
  while (el) {
    const bg = getComputedStyle(el).backgroundColor;
    if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') {
      const match = bg.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
      if (match) {
        return { r: parseInt(match[1]), g: parseInt(match[2]), b: parseInt(match[3]) };
      }
    }
    el = el.parentElement;
  }
  // Default to white if no background found
  return { r: 255, g: 255, b: 255 };
}

function highlightColorTokens() {
  document.querySelectorAll(".md-typeset code").forEach((element) => {
    const text = element.textContent.trim();
    if (!text) {
      return;
    }

    if (isColorToken(text)) {
      const colorRgb = parseColor(text);

      if (colorRgb) {
        // Calculate contrast with white and black
        const whiteRgb = { r: 255, g: 255, b: 255 };
        const blackRgb = { r: 0, g: 0, b: 0 };

        const contrastWithWhite = getContrastRatio(colorRgb, whiteRgb);
        const contrastWithBlack = getContrastRatio(colorRgb, blackRgb);

        // Use whichever has better contrast
        const textColor = contrastWithWhite > contrastWithBlack ? '#ffffff' : '#000000';

        element.style.backgroundColor = text;
        element.style.color = textColor;
        element.style.padding = '0.15rem 0.35rem';
        element.style.borderRadius = '4px';
      }

      element.classList.add("color-token");
    }
  });
}

if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", highlightColorTokens);

  // Re-highlight when theme changes in MkDocs Material
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.type === 'attributes' && mutation.attributeName === 'data-md-color-scheme') {
        highlightColorTokens();
      }
    });
  });

  // Start observing theme changes on the document body
  document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector('body');
    if (body) {
      observer.observe(body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
    }
  });
}
