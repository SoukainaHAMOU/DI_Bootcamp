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
import string
alphabet = string.ascii_lowercase
vowels = ["a", "e", "i", "o", "u"]
for i in range(len(alphabet)):
    if alphabet[i] in vowels :
        print(alphabet[i], "is a vowel")
    elif alphabet[i] == "y" :
        print(alphabet[i], "is considered as a vowel and a consonant")
    else :
        print(alphabet[i], "is a consonant")

#Exercise 6: Words and letters
words = []
for i in range(7):
    word = input("Enter 7 words: ")
    words.append(word)
"""
words = input('Enter 7 words: ')
words = words.split(",")
"""
letter = input("Enter a single letter : ")
for word in words:
    indexx = word.find(letter)
    print('The index of the letter in the words is: ', indexx)
    if indexx == -1:
        print("He! Your letter isn't part of the word.")
    else :
        print(f"The letter {letter} appear at {indexx} in the word {word}")

#Exercise 7: Min, Max, Sum

list_of_numbers = list(range(1, 10**6 + 1))
max_num = max(list_of_numbers)
print('The maximum is:', max_num)
min_num = min(list_of_numbers)
print('The minimum is:', min_num)
sum_num = sum(list_of_numbers)
print('The sum of the numbers is:', sum_num)

#Exercise 8 : List and Tuple
#numbers = 34,67,55,33,12,98
numbers = input('Enter the numbers separated by a comma : ')
num = numbers.split(",")
list_numbers = list(num)
tuple_numbers = tuple(num)
print(list_numbers)
print(tuple_numbers)


#Exercise 9 : Random number
import random
lose = 0
win = 0
while True :
    num = int(input(" Enter a number from 1 to 9: "))
    random_num = random.randint(1, 10)
    if num == 0 :
        break
    elif num == random_num :
        print(f"Congratulation! You get the right number : {num}")
        win += 1
    else: #num != random_num :
        print('Oups! Try again. Next time you can guess the random number')
        lose += 1
print(f"You win {win} times, and you lose {lose} times")


