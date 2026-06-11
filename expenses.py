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
from file_handler import save_expense, load_expenses, save_all_expenses


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
    # Note: amount cleaning (e.g. comma-to-dot conversion) is handled inside validate_amount
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


def get_total_spending():
    """
    Calculate the total amount spent across all recorded expenses.

    Returns:
        float: The sum of all expense amounts.
               Returns 0.0 if there are no expenses.
    """
    # Load all expenses from the CSV file
    expenses = get_all_expenses()

    # Start with a total of zero
    total = 0.0

    # Add each expense amount to the total
    for expense in expenses:
        # Convert amount to float in case it was stored as a string
        total += float(expense["amount"])

    return total


def get_spending_by_category():
    """
    Calculate total spending for each category.

    Returns:
        dict: A dictionary where each key is a category name (str) and each
              value is the total amount spent in that category (float).
              Returns an empty dict if there are no expenses.

    Example:
        {
            "Food": 12000.0,
            "Transport": 5000.0
        }
    """
    # Load all expenses from the CSV file
    expenses = get_all_expenses()

    # Dictionary to hold the running total for each category
    spending = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        # If we haven't seen this category before, start at zero
        if category not in spending:
            spending[category] = 0.0

        # Add this expense's amount to the category total
        spending[category] += amount

    return spending


def get_highest_expense():
    """
    Find and return the expense with the highest amount.

    Returns:
        dict: The expense dictionary with the highest amount.
              Returns None if there are no expenses.
    """
    # Load all expenses from the CSV file
    expenses = get_all_expenses()

    # If there are no expenses, return None
    if not expenses:
        return None

    # Assume the first expense is the highest to start
    highest = expenses[0]

    # Compare each expense to find the one with the largest amount
    for expense in expenses:
        if float(expense["amount"]) > float(highest["amount"]):
            highest = expense

    return highest


def filter_expenses_by_category(category_input):
    """
    Return a list of expenses that belong to the given category.

    The category name is validated first. If it is not one of the
    allowed categories, the function returns None.

    Parameters:
        category_input (str): The category to filter by (e.g. "food", "Transport").

    Returns:
        list[dict] or None:
            A list of expense dictionaries matching the category,
            or None if the category is invalid.
    """
    # Validate the category to ensure it is one of the allowed options
    category = validate_category(category_input)
    if category is None:
        return None

    # Load all expenses from the CSV file
    expenses = get_all_expenses()

    # Build a new list containing only expenses that match the category
    filtered = []
    for expense in expenses:
        if expense["category"] == category:
            filtered.append(expense)

    return filtered


def delete_expense(index):
    """
    Delete an expense from the CSV file at the given index.

    The index is zero-based, meaning index 0 refers to the first expense.
    If the index is out of range, the function returns False and the
    CSV file is left unchanged.

    Parameters:
        index (int): The zero-based position of the expense to delete.

    Returns:
        bool:
            True  – if the expense was successfully deleted.
            False – if the index is invalid (out of range).
    """
    # Load all current expenses
    expenses = get_all_expenses()

    # Check that the index is within a valid range
    if index < 0 or index >= len(expenses):
        return False

    # Remove the expense at the given index
    expenses.pop(index)

    # Rewrite the CSV file with the remaining expenses
    save_all_expenses(expenses)

    return True
