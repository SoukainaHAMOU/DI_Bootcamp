#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

#Exercise 2: Cinemax

total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for keys, values in family.items():
    if values < 3:
        total += 0
        print(f"{keys} will enter for free.")
    elif values >= 3 and  values <= 12:
        total += 10
        print(f"Ticket price for {keys} is {10} ")
    elif values > 12 : 
        total += 15
        print(f"Ticket price for {keys} is {15} ")
    
print(f"The total price of the tickets for all the family members is {total}")

#Bonus:
total = 0
family_mem = int(input("Enter how many family member : "))
family = {}

for i  in range(family_mem):
    name = input("Enter the members name :")
    age = int(input('Enter the age of the members :'))
    family[name] = age

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for keys, values in family.items():
    if values < 3:
        total += 0
        print(f"{keys} will enter for free.")
    elif values >= 3 and  values <= 12:
        total += 10
        print(f"Ticket price for {keys} is {10} ")
    elif values > 12 : 
        total += 15
        print(f"Ticket price for {keys} is {15} ")
    
print(f"The total price of the tickets for all the family members is {total}")

#Exercise 3: Zara
brand = {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        "major_color": {
            "France": "blue", 
            "Spain": "red", 
            "US": ["pink", "green"]

        }
}

brand["number_stores"] = 2
print(f"Zara have clothes for the {brand["type_of_clothes"][0]}, {brand["type_of_clothes"][1]}, {brand["type_of_clothes"][2]} and {brand["type_of_clothes"][3]} ")
brand["country_creation"] = "Spain"
brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand["major_color"]['US'])
print(len(brand.keys()))
print(brand.keys())

for i in brand.keys():
    print(i)

# #Bonus
more_on_zara = {
                "creation_date": 1947,
                "number_stores":2000 ,
}
brand.update(more_on_zara)
print(brand)

#Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#1
users_dict1 = {}
for i in enumerate(users):  
    x,y = tuple(i)  
    users_dict1[x] = y
   
print(users_dict1)
#2
users_dict2 = {}
for i in enumerate(users):  
    x,y = tuple(i)  
    users_dict2[y] = x
print(users_dict2)
#3
users_dict = {}
users.sort()
for i in enumerate(users):  
    x,y = tuple(i)  
    users_dict[y] = x
print(users_dict)