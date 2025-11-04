#Exercise 1 : Hello World-I love Python
print(4*"Hello world\n" + 4*"I love python\n")

#Exercise 2 : What is the Season ?
month = int(input("Enter Month from 1 and 12 : "))
if month >= 3 and month <= 5 :
    print("The season is Spring.") 
elif month >= 6 and month <= 8 :
    print("The season is Summer.")
elif month >= 9 and month <= 11 :
    print("The season is Autumn.")
else :
    print("The season is Winter.")
