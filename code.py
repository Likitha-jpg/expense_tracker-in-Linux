import json
import os

# File to store expense data
DATA_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    date = input("Enter the date (DD-MM-YYYY): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")
    
    expense = {
        'date': date,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

def summarize_expenses(expenses):
    """Summarize the total amount of expenses."""
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def main():
    """Main function to run the expense tracker."""
    expenses = load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            summarize_expenses(expenses)
        elif choice == '4':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
