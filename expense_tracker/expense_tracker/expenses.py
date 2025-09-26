import csv
from models import Expense
from utils import clean_amount, now_str

def add_expense(file_path):
    """Add a new expense to CSV"""
    name = input("Enter expense name: ")
    amount = clean_amount(input("Enter expense amount: "))
    categories = ["🍔 Food", "🏠 Home", "💼 Work", "🎉 Fun", "✨ Misc"]

    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    cat_choice = int(input("Pick a category [1-5]: "))
    category = categories[cat_choice - 1]

    entry = Expense(name=name, amount=amount, category=category, date_time=now_str())

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(entry.to_row(type="expense"))

    print("✅ Expense added!")

def summarize_expenses(file_path, budget):
    """Read expenses and print summary"""
    expenses = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 5 and row[4] == "expense":
                expenses.append(float(row[1]))

    total = sum(expenses)
    print(f"💵 Total Spent: ${total:.2f}")
    print(f"✅ Remaining Budget: ${budget - total:.2f}")
