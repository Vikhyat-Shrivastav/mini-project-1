

name = input("Enter your name: ")

income = float(input("Enter monthly income: "))
rent = float(input("Enter rent: "))
food = float(input("Enter food expenses: "))
travel = float(input("Enter travel expenses: "))
entertainment = float(input("Enter entertainment expenses: "))
other = float(input("Enter other expenses: "))


total_expenses = rent + food + travel + entertainment + other


remaining_money = income - total_expenses


if income > 0:
    savings_percentage = (remaining_money / income) * 100
else:
    savings_percentage = 0

daily_spending = total_expenses / 30
weekly_spending = total_expenses / 4


savings_target = float(input("Enter your savings target: "))


print("\n===== MONTHLY EXPENSE REPORT =====")
print(f"Name: {name}")
print(f"Monthly Income: ₹{income:.2f}")
print(f"Total Expenses: ₹{total_expenses:.2f}")
print(f"Remaining Money: ₹{remaining_money:.2f}")
print(f"Savings Percentage: {savings_percentage:.2f}%")

print(f"Daily Average Spending: ₹{daily_spending:.2f}")
print(f"Weekly Average Spending: ₹{weekly_spending:.2f}")

if remaining_money >= savings_target:
    print("Savings Target: Achieved!")
else:
    print("Savings Target: Not Achieved")

print("==================================")