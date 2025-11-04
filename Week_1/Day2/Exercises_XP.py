#Exercise 1: Favorite Numbers

my_fav_numbers = {1, 6, 5, 7, 9, 10, 19, 96}
my_fav_numbers.add(15)
my_fav_numbers.add(2)
print(my_fav_numbers)
my_fav_numbers.remove(2)

friend_fav_numbers = {2, 4, 6, 7, 9, 15}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
Numbers = (12, 23, 45, 34, 2, 3, 6)
# Numbers.append(4)
print(Numbers)

#Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(0)
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
how_many = basket.count("Apples")
print(how_many)
basket.clear()
print(basket)


#Exercise 4: Floats

#A float is a number that has a decimal point, 
Num = 1.5
lisst = []

while Num <= 5 :
    lisst.append(Num)
    #lisst.append(int(Num) if Num.is_integer() else Num)
    Num += 0.5

print(lisst)

#Exercise 5: For Loop
for x in range(1,21) : 
    print(x)
    x += 1

for x in range(1,21) : 
    if x % 2 == 0 :
        print(x)
    x += 1    

#Exercise 6: While Loop
while True :
    Name = input("Enter your name: ")
    if not Name.isdigit() and len(Name) >= 3:
        print("Thank you")
        break
    else :
        print("Please enter a valid name.")


#Exercise 7: Favorite Fruits

favorite_fruits = input('Enter your favorite fruits, you can enter many fruits: ')
lists_fruit = favorite_fruits.split()


while True: 
    chosen_fruit = input('Enter the name of any fruit: ')
    if chosen_fruit in favorite_fruits:
        print("You chose one of your favorite fruits! Enjoy!")
        break
    else: 
        "You chose a new fruit. I hope you enjoy it!"

#Exercise 8: Pizza Toppings
toppings = []
price = 10
while True:
    topping = input('Enter the pizza toppings one by one :')
    if topping.lower() != "quit":
        toppings.append(topping)
        price += 2.5
        print("Adding", topping, "to your pizza.")

    else :
        break
print("The entire toppings you chose", toppings)
print("Total price: $", price)


#Exercise 9: Cinemax Tickets
price = 0
while True : 
    age = int(input("Enter the age of each person in a family who wants to buy a movie ticket: "))

    if age == 0:
        break
    if age > 12:
        price += 15
    elif age >=3 and age <= 12 :
        price += 10
    else : 
        price += 0

print('The  total ticket cost :', price)

#Bonus

list_of_attendees = []
while True :
    age = int(input("Enter your age: "))
    if age == 0 :
        break    
    elif age >= 16 and age <=21 :
        attendee = input("Enter the name ofthe attendee : ")
        list_of_attendees.append(attendee)
    else : 
        print("you are not allow to enter : ")
print("The list of attendees is :", list_of_attendees)
