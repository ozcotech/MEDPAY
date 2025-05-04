from models.tariff_model import TariffModel
from typing import Optional, Dict, Tuple


# This class is responsible for calculating the mediation fee
# based on tariff data such as monetary brackets, non-monetary types,
# minimum fees, agreement ratios, and serial dispute rules.

# Main class for calculating mediation fees in Turkish legal context.
class FeeCalculator:
    # Initializes the calculator with a TariffModel instance to access tariff data.
    def __init__(self):
        self.model = TariffModel()

    # Calculates the appropriate mediation fee based on input parameters.
    # Parameters:
    # - is_monetary: Indicates if the dispute is monetary.
    # - amount: The amount in dispute (if monetary).
    # - dispute_type: The type of dispute (if non-monetary).
    # - party_key: Identifies whether single or multiple parties are involved.
    # - is_agreement: Whether the dispute was resolved with an agreement.
    # - is_serial: Whether the dispute is part of a serial case group.
    # - category: The category of dispute for minimum and serial fee determination.
    # Returns:
    # - The calculated fee as a float value.
    def calculate_fee(
        self,
        is_monetary: bool,
        amount: Optional[float] = None,
        dispute_type: Optional[str] = None,
        party_key: Optional[str] = None,
        is_agreement: bool = False,
        is_serial: bool = False,
        category: str = "general",
        multiple_mediators: bool = False
    ) -> float:
        fee = 0.0

        if is_monetary:
            if amount is None:
                raise ValueError("Amount must be provided for monetary disputes.")

            # Retrieve monetary brackets and determine the applicable one based on amount.
            brackets = self.model.get_monetary_brackets()
            
            # Loop through each monetary bracket to find the matching range
            for bracket_id, bracket in brackets.items():
                min_amt = bracket["min_amount"]
                max_amt = bracket["max_amount"]
                
                # Choose the appropriate rate based on whether there are multiple mediators
                rate_key = "multiple_mediators" if multiple_mediators else "single_mediator"
                rate = bracket[rate_key]
                
                # Check if the amount falls within this bracket
                if max_amt is None:  # For the highest bracket (26520000+)
                    if amount >= min_amt:
                        fee = amount * (rate / 100)  # Convert percentage to decimal
                        break
                elif min_amt <= amount <= max_amt:
                    fee = amount * (rate / 100)  # Convert percentage to decimal
                    break

        else:
            if not dispute_type or not party_key:
                raise ValueError("Dispute type and party key must be provided for non-monetary disputes.")

            # New logic for non-monetary fee calculation based on agreement and party count
            if is_agreement:
                # Use the 1-hour rate and multiply by 2 for minimum required 2 hours
                one_hour_fee = self.model.get_non_monetary_fee(dispute_type, party_key)
                if one_hour_fee is not None:
                    fee = one_hour_fee * 2
            else:
                # Non-agreement (e.g., state-paid), apply adjusted calculation
                one_hour_fee = self.model.get_non_monetary_fee(dispute_type, party_key)
                if party_key == "2_kisi" and one_hour_fee is not None:
                    fee = one_hour_fee * 2 * 2  # 2 parties * 2 hours
                elif one_hour_fee is not None:
                    fee = one_hour_fee * 2  # Group fee * 2 hours

        # If it's a serial dispute, compare and take the higher fee.
        if is_serial:
            serial_fee = self.model.get_serial_dispute_fee(category)
            fee = max(fee, serial_fee)

        # Ensure the fee is not less than the minimum allowed fee for the given category.
        minimum_fee = self.model.get_minimum_fee(category)
        fee = max(fee, minimum_fee)

        return fee