# Smart Expense Analyzer

## Project Overview

Smart Expense Analyzer is a command-line Python application that helps users record, store, and analyze personal expenses.

The project demonstrates practical Python programming skills including:

* Functions
* Conditionals
* Loops
* File handling
* Lists and dictionaries
* Input validation
* Modular application design

Data is stored locally using CSV files.

---

# Problem Statement

Many students and young professionals struggle to monitor daily spending.

Existing budgeting applications are often:

* Complex
* Internet-dependent
* Overloaded with features

This project provides a lightweight offline solution for recording and analyzing expenses.

---

# Target Users

## Primary User

University students tracking:

* Food
* Transport
* Airtime
* Academic expenses

## Secondary User

Young professionals managing:

* Rent
* Health
* Entertainment
* Personal budgets

---

# Sprint Roadmap

## Sprint 1 (Completed)

### Features

* Add Expense
* View All Expenses
* CSV Storage
* Main Menu
* Input Validation

### Modules

* file_handler.py
* validator.py
* display.py
* expenses.py
* main.py

---

## Sprint 2 (Current)

### Features

* View Total Spending
* View Spending by Category
* Highest Expense Insight

---

## Sprint 3 (Planned)

### Features

* Filter Expenses by Category
* Delete Expense

---

# Folder Structure

smart-expense-analyzer/

├── assets/

├── main.py

├── expenses.py

├── file_handler.py

├── validator.py

├── display.py

├── expenses.csv

├── PROJECT_PROGRESS.md

├── README.md

└── requirements.txt

---

# Architectural Layers

main.py
↓
expenses.py
↓
validator.py
↓
file_handler.py

display.py

main.py communicates with display.py for user interaction.

---

# Design Principles

1. Separation of Concerns
2. Beginner-Friendly Python
3. Procedural Design
4. Single Responsibility per Module
5. CSV-Based Persistence
6. Clear Function Names
7. Incremental Development

---

# Coding Standards

* Use docstrings
* Use meaningful variable names
* Avoid duplicated logic
* Keep functions small and focused
* Commit after completing major milestones

---

# Future Improvements

* Improved currency formatting
* Better category selection
* CSV export enhancements
* Graphical charts
* GUI version
* OOP refactoring
* Database storage
