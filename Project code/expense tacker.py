from typing import List
from expense import Expense

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"

    # Get user input for expense.
    # expense = get_user_expense()

    # Write their expense to a file.
    # save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    Summarize_expenses(expense_file_path)

def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍕 Food",
        "🏠 Home",
        "👔 Work",
        "🎉 Entertainment",
        "🗂 Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def Summarize_expenses(expense_file_path):
    print(f"🎯 Summarizing User Expenses!")
    expenses: List[Expense] = []
    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
           
            if not lines:
                print("No expenses found.")
                return


            total_expense = 0
            expenses = []
            for line in lines:
                expense_name, expense_amount, expense_category = line.strip().split(",")
                print(expense_name, expense_amount, expense_category)
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category,
                )
                print(line_expense)
                expenses.append(line_expense)
                total_expense += float(expense_amount)

            print(f"Total expenses: ${total_expense:.2f}")
    except FileNotFoundError:
        print(f"Expense file not found: {expense_file_path}")

if __name__ == "__main__":
    main()
