from auth import login
from budget import get_or_set_budget
from expenses import add_expense, summarize_expenses
from income import add_income

def main():
    print("🎯 Welcome to Expense Tracker CLI")

    # User login
    user = login()
    print(f"✅ Logged in as: {user}\n")

    # Budget check
    budget = get_or_set_budget("data/budget.csv")

    while True:
        print("\n📌 Main Menu")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice [1-4]: ").strip()
        if choice == "1":
            add_expense("data/expenses.csv")
        elif choice == "2":
            add_income("data/expenses.csv")
        elif choice == "3":
            summarize_expenses("data/expenses.csv", budget)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
