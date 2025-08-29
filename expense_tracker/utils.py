import math

def display_expenses(expenses):
    print("Expenses recorded")
    for expense in expenses:
        print(f"- {expense["item"]:<15} | {expense["amount"]:<7} | {expense["date"]}")
    

def calculate_total_amount_spent(expenses):
    amounts = [expense["amount"] for expense in expenses]
    return math.fsum(amounts)

def calculate_average_amount(expenses):
    total = calculate_total_amount_spent(expenses)
    return round(total/len(expenses), 2)