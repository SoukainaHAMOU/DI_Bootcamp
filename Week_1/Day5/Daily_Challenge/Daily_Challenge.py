#Challenge 1 : Sorting
print("Challenge 1 : ")
user_words= (input("Enter a a single string of words separated by commas (,) : ")).strip()

split_strings = user_words.split(',') #split the string
# sotrted_strings =  sorted(split_strings) #sort the list
# join_sorted_strings = ",".join(sotrted_strings) #Join strings

join_sorted_strings = ",".join(sorted(split_strings))

print(join_sorted_strings) #print the result

#Challenge 2 : Longest word
print("Challenge 2 : ")

user_sentence = input("Enter a sentence : ").strip()

def longest_word(sentence):
    words = sentence.split(" ")  # split the sentence into words
    longest = ""                 # initialize variables

    for word in words:          # iteratz through the words
        if len(word) > len(longest):  # compare word lengths
            longest = word

    return longest    

print("Longest word:", longest_word(user_sentence)) # return the longest word

