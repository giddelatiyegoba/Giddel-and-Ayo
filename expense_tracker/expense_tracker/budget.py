import csv
import datetime
import os

def get_or_set_budget(budget_file_path):
    now = datetime.datetime.now()
    current_month = now.strftime("%Y-%m")

    # If file exists, search for current month
    if os.path.exists(budget_file_path):
        with open(budget_file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2 and row[0] == current_month:
                    return float(row[1])

    # Ask for budget if not set
    while True:
        try:
            raw_budget = input(f"Enter your budget for {current_month}: ").replace(",", "")
            budget = float(raw_budget)
            if budget <= 0:
                print("❌ Budget must be greater than 0.")
                continue

            with open(budget_file_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([current_month, budget])

            return budget
        except ValueError:
            print("❌ Invalid number. Try again.")
