from datetime import datetime

def _format_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def _pretty_print_row(name, time_spent):
    return f"{name} joined {time_spent} years ago"


print("code is in helpers.py")