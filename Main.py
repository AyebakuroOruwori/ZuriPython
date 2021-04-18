
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Budget("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "Vegetables and Fruits")
print(food.get_balance())
clothing = budget.Budget("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing.get_balance())
entertainment = budget.Budget("Entertainment")
food.transfer(50, entertainment)
entertainment.withdraw(25.55)
entertainment.withdraw(100)
print(entertainment.get_balance())
auto = budget.Budget("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(auto.get_balance())

print(food)
print(clothing)
print(entertainment)

print(create_spend_chart([food, clothing,entertainment, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)