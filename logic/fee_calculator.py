from models.tariff_model import TariffModel
from typing import Optional


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
    # Returns:
    # - The calculated fee as a float value.
    def calculate_fee(
        self,
        is_monetary: bool,
        amount: Optional[float],
        dispute_type: Optional[str],
        party_key: str,
        is_agreement: bool,
        is_serial: bool
    ) -> float:
        fee = 0.0

        if is_monetary:
            if amount is None:
                raise ValueError("Amount must be provided for monetary disputes.")

            # Retrieve monetary brackets and determine the applicable one based on amount.
            brackets = self.model.get_monetary_brackets()
            for bracket in brackets:
                if bracket.min <= amount <= bracket.max:
                    fee = bracket.fee
                    break

            # Apply agreement discount ratio if settlement was reached.
            if is_agreement:
                fee *= bracket.agreement_ratio

        else:
            if not dispute_type:
                raise ValueError("Dispute type must be provided for non-monetary disputes.")

            # Retrieve the fee bracket for the specified non-monetary dispute type.
            bracket = self.model.get_non_monetary_fee(dispute_type)
            fee = bracket.get(party_key, 0.0)

        # If it's a serial dispute, compare and take the higher fee.
        if is_serial:
            serial_fee = self.model.get_serial_dispute_fee()
            fee = max(fee, serial_fee)

        # Ensure the fee is not less than the minimum allowed fee.
        minimum_fee = self.model.get_minimum_fee()
        fee = max(fee, minimum_fee)

        return fee