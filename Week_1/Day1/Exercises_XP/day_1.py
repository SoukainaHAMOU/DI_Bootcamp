#Exercise 1: Hello World

print("Hello world\n" *4)

#Exercise 2: Some Math

num = 99
result = (num ^ 3)*8

#Exercise 3: What is the output?

5 < 3 # False
3 == 3 # True
3 == "3" #False
"3" > 3 #Error_Type
"Hello" == "hello"  #False

#Exercise 4: Your computer brand

computer_brand = "hp"
print("I have an", computer_brand, "computer")

#Exercise 5: Your information

name = "Soukaina"
age = 29
shoe_size = 40
info = "My name is {}, and I am {} years old. My shoe size is {}".format(name, age, shoe_size)
print(info)

#Exercise 6: A & B
a = 400
b = 234
if a > b :
    print("Hello world")


 #Exercise 7: Odd or Even

number = int(input("Enter a number: "))
if number % 2 == 0 :
    print(f"The number is {number} is an oven number.")
else:
    print(f"The number is {number} is an odd number.")


#Exercise 8: What’s your name?
Name = input("Enter your name: ")
if Name == "Soukaina":
    print("We share the same name.")
else :
    print("HaHaHa, you have to change your Name.")

#Exercise 9: Tall enough to ride a roller coaster

height = int(input("Enter your height in centemeters: "))

if height > 145 :
    print("You are tall enough to ride.")
else :
    print("Drink milk so you can grow more enough to ride.")
