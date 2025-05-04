# MEDPAY - Mediation Fee Calculator

**Version:** 2025

## 📌 About

**MEDPAY** is a modular, mobile-friendly Python application that calculates mediation fees in accordance with the official Turkish mediation tariff for the year 2025.
It is developed with professional coding standards and supports future tariff updates (2026, 2027...) through a clean and versioned structure.

## 🎯 Purpose

To help legal professionals, mediators, and parties involved in legal disputes accurately and efficiently compute mediation fees based on:

* Dispute type (monetary / non-monetary)
* Agreement status
* Number of parties
* Amount in dispute
* Number of mediators
* Whether the dispute is part of a serial set

## 🧱 Architecture

MEDPAY follows a clean MVC-like separation:

* `constants/` — Contains yearly tariff data (e.g. `tariffs_2025.py`)
* `models/` — Business logic and fee calculation engine
* `screens/` — UI components (Kivy-based)
* `utils/` — Helper methods, type definitions, etc.
* `assets/` — Static assets (icons, fonts, etc.)
* `tests/` — Unit tests
* `main.py` — Entry point for the app

For detailed design principles, see [Software Architecture (EN)](docs/software_architecture.md) or [Mimari Tasarım (TR)](docs/MEDPAY_mimari.md)

## 📊 Tariff System

The 2025 mediation tariff is based on:

* **Section 1:** Non-monetary disputes with flat fees by party count
* **Section 2:** Monetary disputes using tiered percentages based on amount brackets

Minimum and serial dispute fees are also integrated.

## 📱 Technology Stack

* Python 3.10+
* Kivy (for mobile-friendly UI)
* Type hinting and TypedDict for clarity
* Enum and constants for maintainability

## 📦 Installation & Setup (Coming Soon)

This repo will include installation instructions and packaging guides once the UI and logic modules are finalized.

## ✅ Current Status

* [x] Tariff constants defined (`tariffs_2025.py`)
* [x] Folder structure initialized
* [x] Naming conventions standardized (English code / Turkish data)
* [x] TariffModel implemented (`tariff_model.py`)
* [x] FeeCalculator implemented (`fee_calculator.py`)
* [x] FeeController implemented (`fee_controller.py`)
* [ ] UI screens setup
* [ ] Tests and validation

## 🖼️ Screenshots

Below is a placeholder for screenshots and visuals that will demonstrate the user interface of MEDPAY.

_Screenshots will be added once the UI is implemented._

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed by Özkan Cömert ([ozcotech](https://github.com/ozcotech)), 2025

## 🛡️ Trademark Notice

MEDPAY is a trademark of Özkan Cömert.  
All rights to the name and brand identity are reserved by the developer.  
This project is not affiliated with any other entity using similar names.
