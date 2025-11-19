# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## v0.1.9 | 2025-11-19

### Changed

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

### Edited

- Updated dependencies to their latest versions.
- Improved performance of color parsing functions.
- Fixed bug where CSS_MAP was not being initialized correctly in `__init__.py`.

## v0.1.6 | 2025-11-06

### Changed

- Refactored `CSSColor` internals: helper functions were introduced for name/hex
	normalisation and lookups; input validation is stricter and clearer errors (ValueError)
	are raised for invalid inputs. Normalisation accepts `#abc`, `abc`, `#aabbcc`, `aabbcc`.
- Normalisation of color names removes spaces and dashes and lowercases names.
- Improved logging and docstrings in `src/rich_color_ext/css.py`.

## v0.1.5 | 2025-11-05

### Fixed

- Resolved an indentation bug introduced during a refactor that caused import-time
	SyntaxError in `css.py` under certain conditions. Added test runs to verify fixes.

## v0.1.4 | 2025-09-05

### Changed

- Allows Color to parse `rich.color_triplet.ColorTriplet` instances.
- Allows Color to parse `rich.color.Color` instances.

## v0.1.3 | 2025-08-01

### Added

- Introduced `install()`, `uninstall()`, and `is_installed()` functions to allow users to
	control when the extended color parser is active.
