"""
validator.py
Provides validation functions for expense data in the Smart Expense Analyzer.
"""

# The list of categories the user is allowed to choose from
ALLOWED_CATEGORIES = [
    "Food",
    "Transport",
    "Rent",
    "Entertainment",
    "Health",
    "Education",
    "Other",
]


def validate_amount(raw_input):
    """
    Validate and convert a raw string input into a positive float amount.

    Parameters:
        raw_input (str): The string to convert (e.g. "12.50").

    Returns:
        float: The converted amount if it is a valid number greater than 0.
        None:  If the input cannot be converted or is not greater than 0.
    """
    try:
        # Attempt to convert the input string to a float
        amount = float(raw_input)

        # The amount must be greater than zero to be valid
        if amount > 0:
            return amount

        # Return None for zero or negative values
        return None

    except (ValueError, TypeError):
        # Return None if conversion fails (e.g. "abc", None, etc.)
        return None


def validate_category(raw_input):
    """
    Validate a category name against the list of allowed categories.
    Matching is case-insensitive, so "food", "FOOD", and "Food" are all accepted.

    Parameters:
        raw_input (str): The category name to validate.

    Returns:
        str:  The properly formatted category name (e.g. "Food") if valid.
        None: If the input does not match any allowed category.
    """
    # Handle non-string input gracefully
    if not isinstance(raw_input, str):
        return None

    # Strip surrounding whitespace and convert to title case for comparison
    cleaned = raw_input.strip().title()

    # Check if the cleaned input matches any allowed category
    for category in ALLOWED_CATEGORIES:
        if cleaned == category:
            return category

    # Return None if no match was found
    return None


def validate_description(raw_input):
    """
    Clean and validate an expense description string.

    Rules:
        - Remove leading and trailing whitespace.
        - Collapse multiple internal spaces into one.
        - If the result is empty, return "No description".
        - Truncate the description to a maximum of 50 characters.

    Parameters:
        raw_input (str): The raw description string to validate.

    Returns:
        str: A cleaned, valid description string (never empty, max 50 chars).
    """
    # Handle non-string input by converting to string first
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)

    # Remove extra whitespace from both ends
    cleaned = raw_input.strip()

    # Collapse multiple spaces inside the string into single spaces
    # split() without arguments splits on any whitespace and removes empty strings
    cleaned = " ".join(cleaned.split())

    # If the description is empty after cleaning, use the default
    if not cleaned:
        return "No description"

    # Limit the description to 50 characters
    if len(cleaned) > 50:
        cleaned = cleaned[:50]

    return cleaned
