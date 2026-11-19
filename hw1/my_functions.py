lst=[10, 20, 30, 40, 50]

def number(lst):
    return lst[0]
print(number(lst))
print(number(lst))
print(number(lst))
"""
Takes the first value from the list in the function. The arguments call that first value from the list
"""

def food(meal="pizza"):
    return "My favorite food is " + meal
print(food("fries"))
print(food("Chicken"))
print(food("Rice"))
"""
The function takes "pizza" as a default parameter. If not, then the arguments input what the meal would be.
Then prints the food listed in the argument
"""
