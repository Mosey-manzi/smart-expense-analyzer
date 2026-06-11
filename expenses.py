"""
expenses.py
Coordinates validation and file operations for the Smart Expense Analyzer.
This module acts as the bridge between user input, validation rules, and CSV storage.
"""

# Import date from the standard library to stamp each expense with today's date
from datetime import date

# Import validation helpers from validator.py
from validator import validate_amount, validate_category, validate_description

# Import file I/O helpers from file_handler.py
from file_handler import save_expense, load_expenses


def create_expense(amount_input, category_input, description_input):
    """
    Validate the given inputs, build an expense dictionary, and save it to the CSV file.

    Validation is performed in this order:
      1. amount   – must be a positive number.
      2. category – must be one of the allowed categories.
      3. description – cleaned automatically (always valid).

    Parameters:
        amount_input      (str): Raw string representing the expense amount.
        category_input    (str): Raw string representing the expense category.
        description_input (str): Raw string for the expense description.

    Returns:
        tuple:
            (False, "amount")   – if the amount is invalid.
            (False, "category") – if the category is invalid.
            (True,  expense)    – if all fields are valid and the expense was saved.
                                  'expense' is the dictionary that was written to disk.
    """
    # Step 1: Validate the amount
    amount_input = amount_input.replace(",", ".")
    amount = validate_amount(amount_input)
    if amount is None:
        return (False, "amount")

    # Step 2: Validate the category
    category = validate_category(category_input)
    if category is None:
        return (False, "category")

    # Step 3: Validate (clean) the description
    # validate_description always returns a valid string, so no error check is needed
    description = validate_description(description_input)

    # Step 4: Build the expense dictionary with today's date in YYYY-MM-DD format
    expense = {
        "date": date.today().isoformat(),
        "amount": amount,
        "category": category,
        "description": description,
    }

    # Step 5: Save the expense to the CSV file
    save_expense(expense)

    # Step 6: Return success along with the saved expense dictionary
    return (True, expense)


def get_all_expenses():
    """
    Load and return all expenses from the CSV file.

    Returns:
        list[dict]: A list of expense dictionaries, each containing the keys:
                    'date', 'amount', 'category', 'description'.
                    Returns an empty list if the file does not exist or has no data.
    """
    return load_expenses()
