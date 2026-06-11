"""
main.py
Entry point for the Smart Expense Analyzer application.
This module handles the main program loop and user interaction.
"""

# Import display functions for showing information to the user
from display import (
    show_menu,
    show_success_message,
    show_error_message,
    show_expense_table,
    display_spending_by_category,
    display_highest_expense,
)

# Import expense operations for creating, retrieving, and analyzing expenses
from expenses import (
    create_expense,
    get_all_expenses,
    get_total_spending,
    get_spending_by_category,
    get_highest_expense,
)

# Import file handler to ensure the CSV file exists before we start
from file_handler import create_csv_if_missing


def main():
    """
    Main function that runs the Smart Expense Analyzer application.

    This function:
    1. Creates the CSV file if it doesn't exist.
    2. Displays a menu in a loop until the user chooses to exit.
    3. Handles user choices for adding, viewing, and analyzing expenses.
    """
    # Ensure the CSV file exists before we start working with expenses
    create_csv_if_missing()

    # Main program loop - continues until user chooses to exit
    while True:
        # Display the menu options to the user
        show_menu()

        # Get the user's menu choice
        choice = input("\nEnter your choice (1-6): ").strip()

        # --- Sprint 1 Features ---

        # Handle Option 1: Add Expense
        if choice == "1":
            # Ask the user for expense details
            amount_input = input("Enter amount: ").strip()
            category_input = input("Enter category: ").strip()
            description_input = input("Enter description (optional): ").strip()

            # Try to create and save the expense
            success, result = create_expense(amount_input, category_input, description_input)

            # Handle the result based on whether creation succeeded
            if success:
                # result is the expense dictionary on success
                show_success_message(result)
            elif result == "amount":
                # result is the string "amount" if amount validation failed
                show_error_message("amount", "Must be greater than 0")
            elif result == "category":
                # result is the string "category" if category validation failed
                show_error_message("category", "Invalid category")

        # Handle Option 2: View All Expenses
        elif choice == "2":
            # Load all expenses from the CSV file
            expenses = get_all_expenses()

            # Display them in a formatted table
            # (show_expense_table handles the empty case automatically)
            show_expense_table(expenses)

        # --- Sprint 2 Features ---

        # Handle Option 3: View Total Spending
        elif choice == "3":
            # Get the total spending from the expenses module
            total = get_total_spending()

            # Display the total with commas and 2 decimal places
            print(f"\nTotal Spending: {total:,.2f}")

        # Handle Option 4: View Spending by Category
        elif choice == "4":
            # Get the spending breakdown from the expenses module
            spending = get_spending_by_category()

            # Display it using the formatted table from the display module
            display_spending_by_category(spending)

        # Handle Option 5: View Highest Expense
        elif choice == "5":
            # Get the highest expense from the expenses module
            highest = get_highest_expense()

            # Display it using the insight panel from the display module
            display_highest_expense(highest)

        # Handle Option 6: Exit
        elif choice == "6":
            print("\nThank you for using Smart Expense Analyzer. Goodbye!")
            break

        # Handle invalid menu choice
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from 1 to 6.")


# Standard Python entry point check
# This ensures main() only runs when the script is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()
