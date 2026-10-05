# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v3.0.0 | 2026-10-04

### Breaking changes

- **Rich-first parsing.** The patched `Color.parse` now always tries Rich's own
  parser first and only falls back to 3-digit hex and the CSS color map when Rich
  raises `ColorParseError`. Names Rich already knows (`red`, `green`, `blue`,
  `white`, `black`, `yellow`, `magenta`, `cyan`, `orchid`, `tan`, `violet`,
  `purple`, ...) now keep Rich's color (ANSI/256-color) instead of being remapped
  to the CSS truecolor hex. Previously the CSS map took precedence.
- **3-digit hex requires `#`.** `is_3digit_hex()` / `expand_3digit_hex()` and the
  patched parser no longer accept bare `abc`/`09f`, so words like `bad` or `add`
  are never mistaken for colors. Use `#abc`.

### Fixed

- `Color.parse` can be called on a `Color` instance again; the patch is installed as
  a `staticmethod` (it previously failed with a `TypeError`). `uninstall()` now
  restores Rich's original `classmethod` object exactly.

### Changed

- The patched parser is memoised with `functools.lru_cache`, like Rich's own.
- Docstrings, README and docs updated to match; removed dead code paths.
- Ruff/mypy target Python 3.11 (matching `requires-python`); removed the unused
  `loguru` mypy override.
- `install()`/`uninstall()` are serialised with a `threading.Lock`, and
  `is_installed()` now inspects `Color.parse` itself; the `INSTALLED` flag was removed.
- Removed the import-time `CSS_MAP` preload (**breaking** for `from rich_color_ext
  import CSS_MAP`; use `get_css_map()`), and made the `rich.panel`/`table`/`columns`
  imports in `css.py` lazy.
- Added regression tests (instance calls, cache, Rich-first behaviour, bare words).

Includes all changes from v2.0.0 below.

## v2.0.0 | 2026-08-19

### Removed Loguru and updated README.md and Docs

- Bumped `rich-color-ext` to version `v2.0.0` and I made some breaking changes:
- Removed the logger and the cli functionality (Not really aligned with the purpose of this library). That also lead to the removal of the their tests and mentions in the docs.
- Removed the `loguru` dependency, as was not used.
- Updated personal logo.

## v0.1.9 | 2025-11-19

### Fixed Typos

- Bumped the package version to `v0.1.9` in preparation for the next
distribution build.
- Updated the README and documentation landing page to clearly call out the
current release and how to verify what version is installed locally.
- Added links back to this changelog from the README/docs so users can see the
latest changes at a glance.

## v0.1.8 | 2025-11-07

### Added Loguru dependency

- Added `loguru` as a dependency for improved logging capabilities.
- Integrated `loguru` logging into the package, with logging disabled by default.
- Updated documentation to reflect the addition of `loguru`.
- Removed CI configuration (GitHub Actions) from the repository; CI is no longer
provided by the project by default. See repository policies for where CI is
now hosted or how to re-enable it locally.

## v0.1.7 | 2025-11-07

### Updated Dependancies and  Fixed Bugs

- Updated dependencies to their latest versions.
- Improved performance of color parsing functions.
- Fixed bug where CSS_MAP was not being initialized correctly in `__init__.py`.

## v0.1.6 | 2025-11-06

### Refactored and added helper

- Refactored `CSSColor` internals: helper functions were introduced for name/hex
normalisation and lookups; input validation is stricter and clearer errors (ValueError) are raised for invalid inputs. Normalisation accepts `#abc`, `abc`, `#aabbcc`, `aabbcc`.
- Normalisation of color names removes spaces and dashes and lowercases names.
- Improved logging and docstrings in `src/rich_color_ext/css.py`.

## v0.1.5 | 2025-11-05

### Fixed Bug

- Resolved an indentation bug introduced during a refactor that caused import-time SyntaxError in `css.py` under certain conditions. Added test runs to verify fixes.

## v0.1.4 | 2025-09-05

### Expanded rich.color.Color's ability to parse colors

- Allows Color to parse `rich.color_triplet.ColorTriplet` instances.
- Allows Color to parse `rich.color.Color` instances.

## v0.1.3 | 2025-08-01

### Added Installiation Functions

- Introduced `install()`, `uninstall()`, and `is_installed()` functions to allow users to control when the extended color parser is active.
