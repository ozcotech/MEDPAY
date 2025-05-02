"""
2025 Mediation Fee Tariff

This file defines mediation fee brackets used in the MEDPAY application.
It is structured in two main sections:
1. Non-monetary disputes
2. Monetary disputes (tiered rate system)
"""

from typing import Dict, TypedDict, Optional

# Version of the tariff
TARIFF_VERSION: int = 2025

class NonMonetaryBracket(TypedDict):
    """Fees based on the number of parties"""
    _2_parties: float
    _3_to_5_parties: float
    _6_to_10_parties: float
    _11_or_more_parties: float

# Non-monetary disputes
SECTION_ONE: Dict[str, NonMonetaryBracket] = {
    "family_law": {
        "2_parties": 785.00,
        "3_to_5_parties": 1650.00,
        "6_to_10_parties": 1750.00,
        "11_or_more_parties": 1850.00
    },
    "commercial": {
        "2_parties": 1150.00,
        "3_to_5_parties": 2350.00,
        "6_to_10_parties": 2450.00,
        "11_or_more_parties": 2550.00
    },
    "employment_dispute": {
        "2_parties": 785.00,
        "3_to_5_parties": 1650.00,
        "6_to_10_parties": 1750.00,
        "11_or_more_parties": 1850.00
    },
    "consumer": {
        "2_parties": 785.00,
        "3_to_5_parties": 1650.00,
        "6_to_10_parties": 1750.00,
        "11_or_more_parties": 1850.00
    },
    "rental_neighbor_condo": {
        "2_parties": 835.00,
        "3_to_5_parties": 1750.00,
        "6_to_10_parties": 1850.00,
        "11_or_more_parties": 1950.00
    },
    "dissolution_of_partnership": {
        "2_parties": 900.00,
        "3_to_5_parties": 2000.00,
        "6_to_10_parties": 2100.00,
        "11_or_more_parties": 2200.00
    },
    "other": {
        "2_parties": 785.00,
        "3_to_5_parties": 1650.00,
        "6_to_10_parties": 1750.00,
        "11_or_more_parties": 1850.00
    }
}

class MonetaryBracket(TypedDict):
    range_label: str
    single_mediator: float
    multiple_mediators: float
    min_amount: float
    max_amount: Optional[float]

# Monetary disputes
SECTION_TWO: Dict[str, MonetaryBracket] = {
    "1": {"range_label": "0-300000", "single_mediator": 6.0, "multiple_mediators": 9.0, "min_amount": 0.0, "max_amount": 300000.0},
    "2": {"range_label": "300000-780000", "single_mediator": 5.0, "multiple_mediators": 7.5, "min_amount": 300000.0, "max_amount": 780000.0},
    "3": {"range_label": "780000-1560000", "single_mediator": 4.0, "multiple_mediators": 6.0, "min_amount": 780000.0, "max_amount": 1560000.0},
    "4": {"range_label": "1560000-3120000", "single_mediator": 3.0, "multiple_mediators": 4.5, "min_amount": 1560000.0, "max_amount": 3120000.0},
    "5": {"range_label": "3120000-7800000", "single_mediator": 2.0, "multiple_mediators": 3.0, "min_amount": 3120000.0, "max_amount": 7800000.0},
    "6": {"range_label": "7800000-14040000", "single_mediator": 1.5, "multiple_mediators": 2.5, "min_amount": 7800000.0, "max_amount": 14040000.0},
    "7": {"range_label": "14040000-26520000", "single_mediator": 1.0, "multiple_mediators": 1.5, "min_amount": 14040000.0, "max_amount": 26520000.0},
    "8": {"range_label": "26520000+", "single_mediator": 0.5, "multiple_mediators": 1.0, "min_amount": 26520000.0, "max_amount": None}
}

# Minimum fees
MINIMUM_FEES: Dict[str, float] = {
    "general": 6000.00,
    "commercial_or_joint": 9000.00
}

# Fixed fees for serial disputes
SERIAL_DISPUTE_FEES: Dict[str, float] = {
    "commercial": 5000.00,
    "other": 4000.00
}