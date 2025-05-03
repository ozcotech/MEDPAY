"""
Tariff Model for Mediation Fees - 2025
Provides access to tariff data imported from constants.
"""

from typing import Dict, Union, Optional
from constants.tariffs_2025 import (
    TARIFF_VERSION,
    SECTION_ONE,
    SECTION_TWO,
    MINIMUM_FEES,
    SERIAL_DISPUTE_FEES,
    NonMonetaryBracket,
    MonetaryBracket
)


class TariffModel:
    """Provides access to 2025 mediation fee tariff data."""

    def __init__(self) -> None:
        self.version: int = TARIFF_VERSION
        self.non_monetary_disputes: Dict[str, NonMonetaryBracket] = SECTION_ONE
        self.monetary_disputes: Dict[str, MonetaryBracket] = SECTION_TWO
        self.minimum_fees: Dict[str, float] = MINIMUM_FEES
        self.serial_dispute_fees: Dict[str, float] = SERIAL_DISPUTE_FEES

    def get_non_monetary_fee(self, dispute_type: str, party_key: str) -> Optional[float]:
        """Returns the fee for non-monetary disputes based on type and party count."""
        return self.non_monetary_disputes.get(dispute_type, {}).get(party_key)

    def get_monetary_brackets(self) -> Dict[str, MonetaryBracket]:
        """Returns all monetary dispute brackets."""
        return self.monetary_disputes

    def get_minimum_fee(self, category: str) -> float:
        """Returns the minimum fee for a given category."""
        return self.minimum_fees.get(category, 0.0)

    def get_serial_dispute_fee(self, category: str) -> float:
        """Returns the fixed fee for serial disputes."""
        return self.serial_dispute_fees.get(category, 0.0)
