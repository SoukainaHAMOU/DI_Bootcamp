#Challenge 1: Letter Index Dictionary 

word = input("Enter a word : ")
my_dictionary = {}
for index in range(len(word)) :
    letter = word[index]
    if letter not in my_dictionary :
        my_dictionary[letter] = [index]
    else : 
        my_dictionary[letter].append(index)

for i in my_dictionary.keys() :
    print(type(i))
    my_dictionary[letter].sort()
print(my_dictionary)


# for letter in word :
#     indexs = word.index(letter)
#     my_dictionary[letter] = indexs
#     if letter is not in my_dictionary :
#         indexs = word.index(letter)
#         my_dictionary[letter] = indexs 
#     else :
#         index = word.index(letter)
#         indexs.append(index)
      
#Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
basket = []
wallet = int(wallet.replace("$", ""))

for item in items_purchase:
    price = items_purchase[item]
    price = price.replace("$", "")
    price = int(price.replace(",", ""))
    items_purchase[item] = price
    if wallet >= price :
        wallet -= price
        basket.append(item)
        
if basket == []:
    print('The basket is Empty, You are broke.')
else : 
    print("You buy these items: ", sorted(basket))



