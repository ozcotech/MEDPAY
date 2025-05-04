

from logic.fee_calculator import FeeCalculator
from typing import Dict, Any


class FeeController:
    """
    Controller layer that connects user input (e.g., from GUI) with the business logic in FeeCalculator.
    It receives a dictionary of input data, validates or maps it if necessary, and returns the calculated fee.
    """

    def __init__(self):
        self.calculator = FeeCalculator()

    def calculate_fee_from_input(self, data: Dict[str, Any]) -> float:
        """
        Accepts input data from the UI and returns the calculated mediation fee.

        Parameters:
            data (dict): {
                "is_monetary": bool,
                "amount": float (optional),
                "dispute_type": str (optional),
                "party_key": str (optional),
                "is_agreement": bool,
                "is_serial": bool,
                "category": str,
                "multiple_mediators": bool
            }

        Returns:
            float: Calculated mediation fee
        """

        # Extract values with defaults for optional keys
        is_monetary = data.get("is_monetary", False)
        amount = data.get("amount")
        dispute_type = data.get("dispute_type")
        party_key = data.get("party_key")
        is_agreement = data.get("is_agreement", False)
        is_serial = data.get("is_serial", False)
        category = data.get("category", "genel")  # default to 'genel'
        multiple_mediators = data.get("multiple_mediators", False)

        # Call the logic layer
        return self.calculator.calculate_fee(
            is_monetary=is_monetary,
            amount=amount,
            dispute_type=dispute_type,
            party_key=party_key,
            is_agreement=is_agreement,
            is_serial=is_serial,
            category=category,
            multiple_mediators=multiple_mediators
        )