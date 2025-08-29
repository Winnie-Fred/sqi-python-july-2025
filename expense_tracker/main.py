"""
Assignment: Student Expense Tracker

You will build a small program that tracks expenses for students. 
This assignment will test your knowledge of:
- File reading and writing
- JSON module
- math and datetime libraries
- Modules and packages

-----------------------------------------------------------
Requirements:
1. Create a package called expense_tracker with:
    - a module storage.py to handle reading/writing JSON data
    - a module utils.py to handle calculations and formatting
    - a main script main.py that runs the program

2. Each expense has:
    - "item" (str) → e.g., "Textbook"
    - "amount" (float) → e.g., 35.5
    - "date" (str, auto-generated with datetime today’s date in format DD/MM/YYYY)

3. When the program runs:
    a. It should read existing expenses from a JSON file (e.g., "expenses.json").
       If the file does not exist, start with an empty list.
    b. Ask the user to enter 2–3 expenses.
    c. Save the expenses back to the JSON file.
    d. Display:
       - All expenses recorded (with date)
       - The total amount spent (use math.fsum to add precisely)
       - The average amount spent per expense

-----------------------------------------------------------
Example Input (user types this in when program runs):
Item name: Textbook
Amount: 35.5

Item name: Lunch
Amount: 12.25

Item name: Notebook
Amount: 5

-----------------------------------------------------------
Example Output (printed to console):
Expenses recorded:
- Textbook | 35.5 | 26/08/2025
- Lunch    | 12.25 | 26/08/2025
- Notebook | 5.0 | 26/08/2025

Total spent: 52.75
Average per expense: 17.58

Data saved to expenses.json

-----------------------------------------------------------
Example expenses.json file (after program runs):
[
    {"item": "Textbook", "amount": 35.5, "date": "26/08/2025"},
    {"item": "Lunch", "amount": 12.25, "date": "26/08/2025"},
    {"item": "Notebook", "amount": 5.0, "date": "26/08/2025"}
]

-----------------------------------------------------------
Hints:
- Use datetime.datetime.now().strftime("%d/%m/%Y") for date
- Use math.fsum([list of numbers]) for total
- Use round(number, 2) for average
- Use json.load() / json.dump() to handle reading and writing the file
- Remember: Your main script should import functions from your package modules
"""


import datetime

from storage import add_expenses, fetch_expenses, EXPENSES_JSON_FILE
from utils import display_expenses, calculate_total_amount_spent, calculate_average_amount

def main():
    expenses = fetch_expenses()
    while True:
        item = input("Enter the item: ").strip()
        amount = float(input("Enter the amount: "))
        date = datetime.datetime.today().strftime("%d/%m/%Y")
        expenses.append({"item": item, "amount": amount, "date": date})
        add_another_expense = input("Do you want to add another expense? (y/n): ").strip().lower()

        if add_another_expense != "y":
            add_expenses(expenses)
            display_expenses(expenses)
            print(f"Total spent: {calculate_total_amount_spent(expenses)}")
            print(f"Average per expense: {calculate_average_amount(expenses)}")
            print(f"Data saved to {EXPENSES_JSON_FILE}")
            break


if __name__ == "__main__":
    main()




# def calculate_avg(numbers: list[int]):
#     return sum(numbers) / len(numbers)

# print(calculate_avg([1, 8, 289, 34]))
# nums = [1, 8, 289, 34]
# print(calculate_avg(nums))
# numbers = [1, 8, 289, 34]
# print(calculate_avg(numbers))
