expenses = []

print("================================")
print("        EXPENSE TRACKER")
print("================================")

while True:

    amount = input("Enter expense amount (or 'q' to quit): ")

    if amount.lower() == "q":
        break

    expenses.append(float(amount))

total = sum(expenses)

print("\nTotal Expense: ₹", total)