"""
main.py
Entry point for the Smart Expense Analyzer application.
This module handles the main program loop and user interaction.
"""

# Import display functions for showing information to the user
from display import show_menu, show_success_message, show_error_message, show_expense_table

# Import expense operations for creating and retrieving expenses
from expenses import create_expense, get_all_expenses

# Import file handler to ensure the CSV file exists before we start
from file_handler import create_csv_if_missing


def main():
    """
    Main function that runs the Smart Expense Analyzer application.

    This function:
    1. Creates the CSV file if it doesn't exist.
    2. Displays a menu in a loop until the user chooses to exit.
    3. Handles user choices for adding expenses, viewing expenses, or exiting.
    """
    # Ensure the CSV file exists before we start working with expenses
    create_csv_if_missing()

    # Main program loop - continues until user chooses to exit
    while True:
        # Display the menu options to the user
        show_menu()

        # Get the user's menu choice
        choice = input("\nEnter your choice (1-3): ").strip()

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

        # Handle Option 3: Exit
        elif choice == "3":
            print("\nThank you for using Smart Expense Analyzer. Goodbye!")
            break

        # Handle invalid menu choice
        else:
            print("\n[ERROR] Invalid choice. Please enter 1, 2, or 3.")


# Standard Python entry point check
# This ensures main() only runs when the script is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()
