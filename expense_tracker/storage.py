import json

EXPENSES_JSON_FILE = "expenses.json"

def fetch_expenses():
    """
    Read expenses from expenses.json if it exists, else, return an empty list.
    Returns a list of expenses.
    """
    try:
        with open(EXPENSES_JSON_FILE, "r") as f:
            contents = f.read()
    except FileNotFoundError as e:
        return []
    else:
        if contents:
            return json.loads(contents)
        return []



def add_expenses(expenses):
    with open(EXPENSES_JSON_FILE, "w") as f:
        f.write(json.dumps(expenses, indent=4))