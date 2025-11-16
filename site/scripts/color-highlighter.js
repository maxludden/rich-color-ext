function isColorToken(token) {
  const hexPattern = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i;
  return hexPattern.test(token) || CSS.supports?.("color", token);
}

function highlightColorTokens() {
  document.querySelectorAll(".md-typeset code").forEach((element) => {
    const text = element.textContent.trim();
    if (!text) {
      return;
    }

    if (isColorToken(text)) {
      element.style.color = text;
      element.classList.add("color-token");
    }
  });
}

if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", highlightColorTokens);
}
