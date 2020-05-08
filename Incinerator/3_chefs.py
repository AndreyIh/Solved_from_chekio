#!/usr/bin/env checkio --domain=py run 3-chefs

# You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. Each of them can prepare the national food and beverage:
# - JapaneseCook: Sushi and Tea;
# - RussianCook: Dumplings and Compote;
# - ItalianCook: Pizza and Juice.
# Your task is to create 3 different subclasses (one for each chef) which are the children of an AbstractCook and have these methods:
# - add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
# - add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
# - total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
# Every client can choose only one chef.In this mission theAbstract Factorydesign pattern could help.
# 
# Example:
# client_1 = JapaneseCook()
# client_1.add_food(2, 20)
# client_1.add_drink(5, 4)
# client_1.total() == "Sushi: 40, Tea: 20, Total: 60"
# 
# client_2 = RussianCook()
# client_2.add_food(1, 40)
# client_2.add_drink(5, 20)
# client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"
# 
# client_3 = ItalianCook()
# client_3.add_food(2, 20)
# client_3.add_drink(2, 10)
# client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
# 
# 
# 
# All data here will be correct and you don't need to implement the value checking.
# 
# Input:Statements and expressions of the 3 chefs’ classes.
# 
# Output:The behaviour as described.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

class AbstractCook:
    def __init__(self):
        self.food_sum = 0
        self.drink_sum = 0
        
    def add_food(self, food_amount, food_price):
        self.food_sum += food_amount * food_price

        
    def add_drink(self, drink_amount, drink_price):
        self.drink_sum += drink_amount * drink_price
    
    def total(self):
        #print (f"""{self.food}: {self.food_sum}, {self.drink}: {self.drink_sum}, Total: {self.food_sum+self.drink_sum}""")
        return f"""{self.food}: {self.food_sum}, {self.drink}: {self.drink_sum}, Total: {self.food_sum+self.drink_sum}"""

class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = 'Sushi'
        self.drink = 'Tea'

class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = 'Dumplings'
        self.drink = 'Compote'

class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = 'Pizza'
        self.drink = 'Juice'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")