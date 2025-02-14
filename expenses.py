import csv

def add_expense(expense_data):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense_data)
        print("Expense added successfully!")

def show_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter expense description: ")
        amount = input("Enter amount: ")
        add_expense([date, description, amount])
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        print("Exiting the app.")
        break
    else:
        print("Invalid choice.")
