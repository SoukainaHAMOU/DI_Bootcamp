#Exercise 1: Currency Class
print("-"*30)
print("Exercise 1: Currency Class\n")

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}" + ("s" if self.amount != 1 else "")
    
    def __int__(self):
        return self.amount
    
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, (int, float)):
            self.amount += other
            return self
        else:
            return NotImplemented
        
    def __repr__(self):
        return str(self)
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1 + c3)
print("TypeError: Cannot add between Currency type <dollar> and <shekel>")
# TypeError: Cannot add between Currency type <dollar> and <shekel>


print("-"*30)
#Excercice 2:Import
print("Exercise 2: Import\n")
from func import summ
summ(3,4)
print("-"*30)

#Exercise 3: String module
print("Exercise 3: String module\n")
import string
import random
t = string.ascii_lowercase
print(t)
tt = ""
for i in range(5):
    tt += random.choice(t)
print(tt)
print("-"*30)
#    print(random.choice(t)) 

#Exercise 4: Current Date
print("Exercise 4: Current Date\n")
from datetime import datetime
now = datetime.now()
print("Current date: ", now)
print("-"*30)

#Exercise 5: Amount of time left until January 1st
print("Exercise 5: Amount of time left until January 1st\n")
import datetime

now = datetime.datetime.now()
new_date =  datetime.datetime(2026, 1, 1)
time_left = new_date - now
print("Time left until January 1st, 2026: ", time_left)
print("-"*30)

#Exercise 6: Birthday and minutes
print("Exercise 6: Birthday and minutes\n")
import datetime

my_birthday = datetime.datetime(1996,10 ,10)
def minutes_since_birthday(birth_date):
    now = datetime.datetime.now()
    time_since_birthday = now - birth_date
    minutes = time_since_birthday.total_seconds() / 60
    return minutes
print("Minutes since my birthday: ", minutes_since_birthday(my_birthday))
print("-"*30)

#Exercise 7: Faker Module
print("Exercise 7: Faker Module\n")

from faker import Faker
users = []
fake = Faker()
def add_user(number_users):
    for number in range(number_users):
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users.append(user)
add_user(5)
print(users)
for user in users:
    for keys, values in user.items():
        print(f"{keys}: {values}")
    print("-"*20)

