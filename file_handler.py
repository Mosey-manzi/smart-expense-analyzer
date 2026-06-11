"""
file_handler.py
Handles all CSV file operations for the Smart Expense Analyzer.
"""

import csv
import os

# Constant: the name of the CSV file used to store expenses
CSV_FILE = "expenses.csv"

# The header row for the CSV file
FIELDNAMES = ["date", "amount", "category", "description"]


def create_csv_if_missing():
    """
    Create the expenses.csv file with a header row if it does not already exist.
    This ensures the file is ready before we try to read from or write to it.
    """
    if not os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
            print(f"Created new CSV file: {CSV_FILE}")
        except IOError as e:
            print(f"Error creating CSV file: {e}")


def load_expenses():
    """
    Load all expenses from the CSV file and return them as a list of dictionaries.
    Each dictionary represents one expense row with keys: date, amount, category, description.
    Returns an empty list if the file does not exist or an error occurs.
    """
    expenses = []

    # Make sure the file exists before trying to read it
    if not os.path.exists(CSV_FILE):
        print("No expenses file found. Returning empty list.")
        return expenses

    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except IOError as e:
        print(f"Error reading CSV file: {e}")

    return expenses


def save_expense(expense):
    """
    Append a single expense dictionary to the CSV file without overwriting existing data.
    The expense should be a dictionary with keys: date, amount, category, description.
    """
    try:
        # Open the file in append mode so existing data is preserved
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow(expense)
        print("Expense saved successfully.")
    except IOError as e:
        print(f"Error saving expense to CSV file: {e}")


def save_all_expenses(expenses):
    """
    Overwrite the entire CSV file with the given list of expenses.
    This is used when we need to remove or modify existing rows.

    Parameters:
        expenses (list[dict]): The complete list of expense dictionaries
                               to write to the CSV file.
    """
    try:
        # Open the file in write mode to replace all contents
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
    except IOError as e:
        print(f"Error rewriting CSV file: {e}")
