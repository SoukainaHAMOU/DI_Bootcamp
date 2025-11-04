#Exercise 1: Concatenate lists

liste1 = [2, 3, 6, 8, 9]
liste2 = [7, 3, 4, 6, 9]
#list = liste1.append(liste2)
list = liste1.extend(liste2)
print(liste1)

#Exercise 2: Range of numbers

for i in range(1500, 2501):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

#Exercise 3: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
while True:
    name = input("Enter your name : ")
    if name.capitalize() in names:
        ind = names.index(name.capitalize())
        print("the index is", ind)
        break
    else :
        print("try again")

#Exercise 4: Greatest Number


number1 = int(input('Enter number 1 : '))
number2 = int(input('Enter number 2 : '))
number3 = int(input('Enter number 3 : '))
if number1 > number2 and number1 > number3 :
    print("The greatest number is: ", number1)
elif number2 > number1 and number2 > number3 :
    print("The greatest number is: ", number1)
else :
    print("The greatest number is: ", number3)


#Exercise 5: The Alphabet
