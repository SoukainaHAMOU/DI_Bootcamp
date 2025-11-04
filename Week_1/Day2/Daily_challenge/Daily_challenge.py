#Challenge 1: Multiples of a Number

number = int(input("Enter a number : "))
length =  int(input('Enter a lenth : '))
liste_of_number = []
for i in range(length) :
    num = number * (i+1)
    liste_of_number.append(num)
print("This is the list of the numbers : ", liste_of_number )


#Challenge 2: Remove Consecutive Duplicate Letters
y = ""
word = input("Enter a word : ")

for i in range(len(word)):
    x = word[i]
    if x != word[i-1] or i == 0 :
        y += word[i]
    
print(y)