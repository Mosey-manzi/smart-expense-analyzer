"""
display.py
Handles all console output for the Smart Expense Analyzer.
This module only prints information to the screen — it does not read input,
perform file operations, or run any validation logic.
"""

# Import the allowed categories so show_categories() stays in sync with validator.py
from validator import ALLOWED_CATEGORIES


def show_menu():
    """
    Display the main program menu with three options:
      1. Add Expense
      2. View All Expenses
      3. Exit
    """
    print("\n===== Smart Expense Analyzer =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")
    print("==================================")


def show_categories():
    """
    Display all allowed expense categories as a numbered list.
    The list is sourced from the ALLOWED_CATEGORIES constant in validator.py.

    Example output:
        Allowed Categories:
          1. Food
          2. Transport
          ...
    """
    print("\nAllowed Categories:")
    for index, category in enumerate(ALLOWED_CATEGORIES, start=1):
        print(f"  {index}. {category}")


def show_empty_message():
    """
    Display a friendly message when there are no expenses recorded yet.
    """
    print("\nNo expenses found. Start by adding your first expense!")


def show_success_message(expense):
    """
    Display a success message after an expense has been saved.

    Parameters:
        expense (dict): The saved expense dictionary.
                        Expected keys: 'amount' and 'category'.
    """
    amount = expense.get("amount", "N/A")
    category = expense.get("category", "N/A")
    print(f"\nExpense of {amount} added successfully under '{category}'.")


def show_error_message(field, reason):
    """
    Display a formatted validation error message for a specific field.

    Parameters:
        field  (str): The name of the field that failed validation (e.g. "amount").
        reason (str): A human-readable explanation of why the value was invalid.
    """
    print(f"\n[ERROR] Invalid {field}: {reason}")


def show_expense_table(expenses):
    """
    Display a list of expenses in a readable, formatted table.

    Each row shows a row number, date, category, amount, and description.
    If the list is empty, show_empty_message() is called instead.

    Parameters:
        expenses (list[dict]): A list of expense dictionaries.
                               Each dict should have keys:
                               'date', 'category', 'amount', 'description'.
    """
    # If there are no expenses, show the friendly empty message and stop
    if not expenses:
        show_empty_message()
        return

    # Print the table header with fixed column widths for alignment
    print("\n{:<5} {:<12} {:<15} {:<12} {}".format(
        "No.", "Date", "Category", "Amount", "Description"
    ))
    # Print a separator line that spans the full table width
    print("-" * 70)

    # Loop through each expense, keeping track of the row number
    for index, expense in enumerate(expenses, start=1):
        date = expense.get("date", "N/A")
        category = expense.get("category", "N/A")
        amount = expense.get("amount", "N/A")
        description = expense.get("description", "N/A")

        # Print each row with the same fixed column widths
        print("{:<5} {:<12} {:<15} {:<12} {}".format(
            index, date, category, amount, description
        ))

    # Print a footer showing the total number of expenses
    print("-" * 70)
    print(f"Total expenses: {len(expenses)}")
