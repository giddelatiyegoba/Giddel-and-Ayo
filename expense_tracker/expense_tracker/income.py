import csv
from models import Income
from utils import clean_amount, now_str

def add_income(file_path):
    """Add new income (cash source)"""
    source = input("Enter income source (e.g., Salary, Gift): ")
    amount = clean_amount(input("Enter income amount: "))

    entry = Income(name=source, amount=amount, date_time=now_str())

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(entry.to_row(type="income"))

    print("✅ Income added!")
