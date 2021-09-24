"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog."""

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.

    amount=questionary.text("How much money would you like to withdraw?")
    amount=float(amount)
    
    
    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.

    if amount <=0.0:
        sys.exit(f"Error: Invalid quantity {amount}")
    
    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.

    if amount <= account["balance"]:
        account["balance"] -= amount
        return account
    else:
        sys.exit(f"Error: Insufficient balance")
        