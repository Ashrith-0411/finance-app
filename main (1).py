import getpass
from database import Database
from user import User
from transaction import Transaction
from budget import Budget
from report import Report

def main_menu(user):
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Set Budget")
        print("4. View Budget")
        print("5. Generate Report")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(user)
        elif choice == '2':
            view_transactions(user)
        elif choice == '3':
            set_budget(user)
        elif choice == '4':
            view_budget(user)
        elif choice == '5':
            generate_report(user)
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction(user):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    transaction_type = input("Enter type (income/expense): ").lower()

    if transaction_type not in ['income', 'expense']:
        print("Invalid transaction type. Please use 'income' or 'expense'.")
        return

    Transaction.add_transaction(user.id, amount, category, description, transaction_type)
    print("Transaction added successfully.")

def view_transactions(user):
    transactions = Transaction.get_transactions(user.id)
    if not transactions:
        print("No transactions found.")
        return

    for t in transactions:
        print(f"ID: {t[0]}, Amount: {t[2]}, Category: {t[3]}, Description: {t[4]}, Type: {t[5]}, Date: {t[6]}")

def set_budget(user):
    category = input("Enter category: ")
    amount = float(input("Enter budget amount: "))
    Budget.set_budget(user.id, category, amount)
    print("Budget set successfully.")

def view_budget(user):
    budgets = Budget.get_budgets(user.id)
    if not budgets:
        print("No budgets found.")
        return

    for b in budgets:
        print(f"Category: {b[2]}, Amount: {b[3]}")

def generate_report(user):
    report_type = input("Enter report type (monthly/yearly): ").lower()
    if report_type not in ['monthly', 'yearly']:
        print("Invalid report type. Please use 'monthly' or 'yearly'.")
        return

    year = int(input("Enter year: "))
    if report_type == 'monthly':
        month = int(input("Enter month (1-12): "))
        report = Report.generate_monthly_report(user.id, year, month)
    else:
        report = Report.generate_yearly_report(user.id, year)

    print("\n--- Financial Report ---")
    print(f"Total Income: {report['total_income']}")
    print(f"Total Expenses: {report['total_expenses']}")
    print(f"Savings: {report['savings']}")
    print("\nCategory-wise Expenses:")
    for category, amount in report['category_expenses'].items():
        print(f"{category}: {amount}")

def main():
    db = Database()
    db.create_tables()

    while True:
        print("\n--- Welcome to Personal Finance Manager ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = User.login(username, password)
            if user:
                print(f"Welcome, {user.username}!")
                main_menu(user)
            else:
                print("Invalid credentials. Please try again.")
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            confirm_password = getpass.getpass("Confirm password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
            else:
                user = User.register(username, password)
                if user:
                    print(f"Registration successful. Welcome, {user.username}!")
                    main_menu(user)
                else:
                    print("Username already exists. Please choose a different username.")
        elif choice == '3':
            print("Thank you for using Personal Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()