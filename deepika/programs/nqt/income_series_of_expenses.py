"""Write a program that takes user income and a series of expenses, then calculates:
• Total income
• Total expenses
• Total savings
• Breakdown of expenses by category
Input:
Enter income: 1000$
Enter expense and type or done: food
Enter price of expense: 200$
Enter expense and type or done: transport
Enter price of expense: 150$
Enter expense and type or done: done
Output:
Summary of expenses:
Total income: 1000$
Total expenses: 350$
Total savings: 650$
Analysis:
Expense and price:
- food: 200$
-transport: 150$"""

income = int(input("enter income:"))
# num_expenses = int(input("enter the value:"))
total_expenses = 0
expense_price_dict = {}

while True:
    expense_type = input("enter expenses and type or done:")
    if expense_type == "done":
        break
    price = int(input("enter the price of expenses:"))
    total_expenses = total_expenses + price
    expense_price_dict[expense_type] = price

savings = income - total_expenses
print("Summary of expenses:")
print(f"Total income: ${income}")
print(f"Total expenses: ${total_expenses}")
print(f"Total savings: ${savings}")
print("Analysis:")
print("Expense and price:")
for item in expense_price_dict.items():
    print(f"-{item[0]}: {item[1]}$")