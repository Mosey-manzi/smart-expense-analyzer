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
    show_total_spending,
    show_deletion_success,
    show_deletion_error,
)

# Import expense operations for creating, retrieving, analyzing, and managing expenses
from expenses import (
    create_expense,
    get_all_expenses,
    get_total_spending,
    get_spending_by_category,
    get_highest_expense,
    filter_expenses_by_category,
    delete_expense,
)

# Import file handler to ensure the CSV file exists before we start
from file_handler import create_csv_if_missing


def main():
    """
    Main function that runs the Smart Expense Analyzer application.

    This function:
    1. Creates the CSV file if it doesn't exist.
    2. Displays a menu in a loop until the user chooses to exit.
    3. Handles user choices for adding, viewing, analyzing, and managing expenses.
    """
    # Ensure the CSV file exists before we start working with expenses
    create_csv_if_missing()

    # Main program loop - continues until user chooses to exit
    while True:
        # Display the menu options to the user
        show_menu()

        # Get the user's menu choice
        choice = input("\nEnter your choice (1-8): ").strip()

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

            # Display the formatted total using the display module
            show_total_spending(total)

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

        # --- Sprint 3 Features ---

        # Handle Option 6: Filter Expenses by Category
        elif choice == "6":
            # Ask the user which category to filter by
            category_input = input("Enter category to filter by: ").strip()

            # Get filtered expenses from the expenses module
            filtered = filter_expenses_by_category(category_input)

            # If the category was invalid, show an error message
            if filtered is None:
                show_error_message("category", "Invalid category")
            else:
                # Display the filtered list in a table
                show_expense_table(filtered)

        # Handle Option 7: Delete Expense
        elif choice == "7":
            # Show all expenses first so the user can see which one to delete
            expenses = get_all_expenses()
            show_expense_table(expenses)

            # Only ask for a number if there are expenses to delete
            if expenses:
                # Ask the user which expense number to delete
                number_input = input("\nEnter expense number to delete: ").strip()

                try:
                    # Convert the user's input to an integer
                    expense_number = int(number_input)

                    # Convert the 1-based display number to a 0-based index
                    index = expense_number - 1

                    # Attempt to delete the expense
                    if delete_expense(index):
                        show_deletion_success()
                    else:
                        show_deletion_error()

                except ValueError:
                    # The user entered something that is not a number
                    show_deletion_error()

        # Handle Option 8: Exit
        elif choice == "8":
            print("\nThank you for using Smart Expense Analyzer. Goodbye!")
            break

        # Handle invalid menu choice
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from 1 to 8.")


# Standard Python entry point check
# This ensures main() only runs when the script is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()
