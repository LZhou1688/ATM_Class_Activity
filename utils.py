"""Helper functions for loading accounts and validating PIN number."""

import csv
from pathlib import Path
import sys


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 6 digits long."""
    if len(pin)==6:
        print("PIN is valid!")
        return True
    else:
        return False
  
if __name__ == "__main__":
    print(validate_pin("16543543152"))
    print(validate_pin("1542"))
    print(validate_pin("165485"))
    
    # @TODO: Verifies length of pin is 6 digits, prints validations message and returns True. Else returns False.
