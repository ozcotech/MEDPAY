# MEDPAY Software Architecture

## Overview
MEDPAY is a modular and extensible Python application designed to calculate mediation fees based on Turkish legal tariffs. It follows a clean architectural pattern that separates data, logic, and presentation for long-term maintainability and clarity.

## Architectural Pattern
MEDPAY is structured using a Model-View-Controller (MVC)-inspired separation:

- **Models** (`models/`):
  - `TariffModel`: Manages tariff data access for different years.
  - `CalculationModel`: Performs fee calculations based on dispute attributes.
  - `DisputeModel`: Represents dispute metadata (type, amount, party count, etc.)

- **Views** (`screens/`):
  - Kivy-based screens for each step of the user interaction:
    - Entry screen
    - Dispute type selector
    - Agreement status selector
    - Party info form
    - Result screen

- **Controllers** (`controllers/`, `main.py`, and utilities):
  - Contains logic handlers for user actions
  - Manages app flow and screen transitions
  - Passes data between UI and model layers

## Constants Layer
- Located in `constants/`
- Each year's tariff data is separated into files like `tariffs_2025.py`
- Easily extendable by adding `tariffs_2026.py`, etc.
- Supports `SECTION_ONE`, `SECTION_TWO`, minimum fees, serial dispute fees, and monetary brackets.

## Naming Conventions
- All class, variable, and file names use English.
- Output values (e.g., dispute labels) are Turkish, to serve domestic users.
- Type hinting and TypedDicts are used for data clarity.

## Versioning
- Each tariff file includes a version constant (e.g., `TARIFF_VERSION = 2025`)
- Future logic will allow year-based tariff switching via `TariffModel`

## Future Improvements
- Enum usage for standardized dispute keys
- Internationalization (i18n) support
- Persistent user settings and dark/light themes
