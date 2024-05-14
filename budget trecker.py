


import json

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount, transaction_type):
        transaction = {
            "category": category,
            "amount": amount,
            "type": transaction_type
        }
        self.transactions.append(transaction)

    def calculate_budget(self, income):
        total_expense = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        remaining_budget = income - total_expense
        return remaining_budget

    def analyze_expenses(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                category = transaction['category']
                amount = transaction['amount']
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount
        return expense_categories

    def save_transactions(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.transactions, f)

    def load_transactions(self, filename):
        with open(filename, 'r') as f:
            self.transactions = json.load(f)

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Add Transaction")
        print("2. Calculate Remaining Budget")
        print("3. Analyze Expenses")
        print("4. Save Transactions")
        print("5. Load Transactions")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            category = input("Enter category (expense/income): ")
            amount = float(input("Enter amount: "))
            transaction_type = 'expense' if category.lower() == 'expense' else 'income'
            budget_tracker.add_transaction(category, amount, transaction_type)
            print("Transaction added successfully.")

        elif choice == '2':
            income = float(input("Enter your income: "))
            remaining_budget = budget_tracker.calculate_budget(income)
            print("Remaining budget:", remaining_budget)

        elif choice == '3':
            expense_categories = budget_tracker.analyze_expenses()
            print("Expense Analysis:")
            for category, amount in expense_categories.items():
                print(f"{category}: {amount}")

        elif choice == '4':
            filename = input("Enter filename to save transactions: ")
            budget_tracker.save_transactions(filename)
            print("Transactions saved successfully.")

        elif choice == '5':
            filename = input("Enter filename to load transactions: ")
            budget_tracker.load_transactions(filename)
            print("Transactions loaded successfully.")

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()SSS