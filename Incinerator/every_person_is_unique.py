#!/usr/bin/env checkio --domain=py run every-person-is-unique

# pre.example {        border: 1px solid #aaa;        border-radius: 3px;        background: #eee;        margin-left: 20px;        padding: 5px;        overflow: auto;    }    p.indent {        margin-left: 20px;    }Every year, the number of your friends is increasing and monitoring information about their lives is becoming more difficult. Let's simplify and slightly automate this process. Indeed, the simplification of routine processes is one of the key programming tasks.
# 
# You have to create a class ‘Person’ and a few methods to work with its instances. See the class description below.
# 
# classPerson(first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')
# 
# It returns a new instance  of the ‘Person’ class  with the name and surname [first_name,last_name], date of birth -birth_date(in 'dd.mm.yyyy' format), current job -job, number of working years -working_years, average salary -salary(per month), current country and city - [country,city] and gender -gender. The gender parameter could be 'male' or 'female'. If this parameter is undefined, the default value is - 'unknown'.
# 
# 
# Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’) ==
# Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’)
# 
# Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’) ==
# Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’, ‘unknown’)
# 
# name()
# 
# Returns the full name (name and surname, separated by a whitespace).
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).name() == ‘John Smith’
# 
# age()
# 
# Returns the person’s age - the number of fully lived years. (The current date is 01.01.2018)
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).age() == 38
# 
# work()
# 
# Returns the person’s job in a sentence as follows:‘He is a ...’ (if male)‘She is a ...’ (if female)‘Is a ...’ (if unknown)
# 
# 
# Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).work() == ‘Is a designer’
# 
# money()
# 
# Returns an amount of money, earned during the working years. It should be returned in format xx xxx … - every 3 decimal places should be separated by a whitespace. For example:‘10 568’‘1 051 422’
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648 000’
# 
# home()
# 
# Returns the country and the city where a person lives:‘Lives in the city, country’
# 
# 
# Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).home() == ‘Lives in Vienna, Austria’
# 
# In this mission all data will be correct and you won't need to implement the value checking.
# 
# Input:Statements and expressions that use the ‘Person’ class.
# 
# Output:The behaviour of an instance as described above.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

from datetime import *
date_0 = datetime.strptime('01.01.2018', '%d.%m.%Y').date()

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name   
        self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        self.job = job
        self.working_years =  working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender
    
    def name(self):
        return f'{self.first_name} {self.last_name}'
        
    def age(self):
        delta = date_0 - self.birth_date
        return int(delta.days // 365.2)
        
    def work(self):
        dict0 = {'male':'He is a','female':'She is a', 'unknown':'Is a'}
        return f'{dict0.get(self.gender)} {self.job}'
    
    def money(self):
        money = str(self.working_years * 12 * self.salary)
        money_1 = ''.join(list(' ' + j if (i % 3) - len(money) % 3 == 0 else j for i,j in enumerate(money))) 
        return money_1.strip()
        
    def home(self):
        return f'Lives in {self.city}, {self.country}'