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
    Display the main program menu with eight options:
      1. Add Expense
      2. View All Expenses
      3. View Total Spending
      4. View Spending by Category
      5. View Highest Expense
      6. Filter Expenses by Category
      7. Delete Expense
      8. Exit
    """
    print("\n===== Smart Expense Analyzer =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. View Highest Expense")
    print("6. Filter Expenses by Category")
    print("7. Delete Expense")
    print("8. Exit")
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


def display_spending_by_category(spending_dict):
    """
    Display a formatted table showing total spending per category.

    Parameters:
        spending_dict (dict): A dictionary where each key is a category name (str)
                              and each value is the total amount spent (float).
                              Example: {"Food": 12000.0, "Transport": 5000.0}
    """
    # If the dictionary is empty, show the friendly empty message and stop
    if not spending_dict:
        show_empty_message()
        return

    # Print the table header with fixed column widths for neat alignment
    print("\n{:<15} {:>15}".format("Category", "Amount"))
    # Print a separator line
    print("-" * 32)

    # Keep track of the total spending across all categories
    total = 0.0

    # Loop through each category and its amount
    for category, amount in spending_dict.items():
        # Add this category's amount to the running total
        total += amount
        # Format the amount with commas and 2 decimal places (e.g. 12,000.00)
        formatted_amount = f"{amount:,.2f}"
        # Print the row with left-aligned category and right-aligned amount
        print("{:<15} {:>15}".format(category, formatted_amount))

    # Print a separator line before the total
    print("-" * 32)
    # Format and display the total spending
    formatted_total = f"{total:,.2f}"
    print("{:<15} {:>15}".format("Total", formatted_total))


def display_highest_expense(expense):
    """
    Display a formatted insight panel showing the highest expense.

    Parameters:
        expense (dict or None): An expense dictionary with keys 'amount',
                                'category', 'description', and 'date',
                                or None if there are no expenses.
    """
    # If no expense was provided, show the friendly empty message and stop
    if expense is None:
        show_empty_message()
        return

    # Extract values from the expense dictionary
    amount = expense.get("amount", 0)
    category = expense.get("category", "N/A")
    description = expense.get("description", "N/A")
    date = expense.get("date", "N/A")

    # Format the amount with commas and 2 decimal places (e.g. 25,000.00)
    formatted_amount = f"{float(amount):,.2f}"

    # Print the insight panel with a header, details, and separators
    print("\nHighest Expense Insight")
    print("-" * 32)
    print(f"  Amount      : {formatted_amount}")
    print(f"  Category    : {category}")
    print(f"  Description : {description}")
    print(f"  Date        : {date}")
    print("-" * 32)


def show_total_spending(total):
    """
    Display the total spending amount with proper number formatting.

    Parameters:
        total (float): The total amount spent across all expenses.
    """
    # Format the amount with commas and 2 decimal places (e.g. 12,345.00)
    print(f"\nTotal Spending: {total:,.2f}")


def show_deletion_success():
    """
    Display a success message when an expense has been deleted.
    """
    print("\nExpense deleted successfully.")


def show_deletion_error():
    """
    Display an error message when expense deletion fails
    (e.g. the provided index was out of range).
    """
    print("\n[ERROR] Could not delete expense. Please enter a valid expense number.")
