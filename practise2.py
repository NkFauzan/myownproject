
salary = 0
other_income = 0
rent = 0
car_payment = 0
groceries = 0
utilities = 0
other_expenses = 0

month = input("Enter the month for your budget: ")


salary = float(input("Enter your salary: "))
other_income = float(input("Enter any other income: "))
house_rent = float(input("Enter your house rent: "))
car_rent = float(input("Enter your car rent: "))
groceries = float(input("Enter your grocery expenses: "))
eletric_waterBill = float(input("Enter your electric and water bill: "))
other_expenses = float(input("Enter any other expenses: "))


gross_income = salary + other_income
total_expenses = house_rent + car_rent + groceries + eletric_waterBill + other_expenses
net_income = gross_income - total_expenses
balance = net_income - total_expenses


if balance > 2000:
  print("Remember to save at least 10% of your account balance!")
elif balance < 500:
  print("youre in danger")
elif balance >= 500 and balance <= 2000:
  print("you need to carefull")
elif balance > 200:
  print("you can start saving now")

print("Budget for", month)
print("Total income:", gross_income)
print("Total expenses:", total_expenses)
print("Account balance:", net_income)
