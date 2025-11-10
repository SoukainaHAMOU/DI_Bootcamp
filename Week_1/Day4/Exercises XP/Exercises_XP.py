#Exercise 1: What Are You Learning?
def display_message() :
    print("I am learning about functions in Python.")

display_message()

#Exercise 2: What’s Your Favorite Book?
def favorite_book(title) :
    print(f"One of my favorite books is: {title}")

favorite_book("Alice in Wonderland")

#Exercise 3: Some Geography
def describe_city(city, country = "Unknown") :
    print(f"{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Pariss")

#Exercise 4: Random
import random
def random_num(num):
    rand = random.randint(1, 100)
    if num == rand:
        print('Success!')
    else:
        print(f"Fail! Your number: {num}, Random number: {23}")

random_num(50)

#Exercise 5: Let’s Create Some Personalized Shirts!
# def make_shirt(size, text):
#     print(f"The shirt size is {size} and the text is: '{text}'.")

# make_shirt("Large", "I love Python")

def make_shirt(size = "large", text = "I love Python"):
    print(f"The shirt size is {size} and the text is: {text}.")

make_shirt("large")
make_shirt("medium")
make_shirt('Large', "Python is my world")

#Exercise 6: Magicians…
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names) :
    for name in names :
        print(name)


def make_great(names):
    for i in range(len(names)) :
        names [i] = (f"The great {names[i]}")

make_great(magician_names)
show_magicians(magician_names)

#Exercise 7: Temperature Advice


# def get_random_temp(a,b) :
#     rand = random.randint(a, b)
#     #rand = random.randint(-10, 40)
#     #print(f"{rand}  degrees Celsius")
#     return rand

# def main() :
#     rand = get_random_temp(-10, 40)
#     print(f"The temperature right now is {rand} degrees Celsius.")
#     if rand < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif rand >= 0 and rand <= 16: 
#         print("Quite chilly! Don't forget your coat.")
#     elif rand  >= 16 and rand <= 23: 
#         print("Nice weather.")
#     elif rand  >= 24 and rand <= 32: 
#         print("A bit warm, stay hydrated.")
#     else : 
#         print("It’s really hot! Stay cool.")
# main()
#Step 4: Floating-Point Temperatures (Bonus)

# def get_random_temp(a,b) :
#     rand = round(random.uniform(a, b),2)
#     return rand

# def main() :
#     rand = get_random_temp(-10, 40)
#     print(f"The temperature right now is {rand} degrees Celsius.")
#     if rand < 0:
#         print("Brrr, that's freezing! Wear some extra layers today.")
#     elif rand >= 0 and rand <= 16: 
#         print("Quite chilly! Don't forget your coat.")
#     elif rand  >= 16 and rand <= 23: 
#         print("Nice weather.")
#     elif rand  >= 24 and rand <= 32: 
#         print("A bit warm, stay hydrated.")
#     else : 
#         print("It's really hot! Stay cool.")
# main()

#
month = int(input("Enter the month: "))
if month >= 10 and month <= 12:
    season = "Autumn"
elif month >= 1 and month <= 3:
    season = "Winter"
elif month >= 4 and month <= 6:
    season = "Spring"
else : 
    season = "Summer"

def get_random_temp(season) :
    if season == "Autumn":
        a,b = (10,20)
    elif season == "Winter":
        a,b = (-5,20)
    elif season == "Spring":
        a,b = (10,20)
    else :
        a,b = (25, 40)

    rand = round(random.uniform(a, b),2)
    return rand

def main() :
    rand = get_random_temp(season)
    print(f"The temperature right now is {rand} degrees Celsius.")
    if rand < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif rand >= 0 and rand <= 16: 
        print("Quite chilly! Don't forget your coat.")
    elif rand  >= 16 and rand <= 23: 
        print("Nice weather.")
    elif rand  >= 24 and rand <= 32: 
        print("A bit warm, stay hydrated.")
    else : 
        print("It's really hot! Stay cool.")
main()