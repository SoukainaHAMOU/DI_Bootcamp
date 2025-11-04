#Exercise 4 : How many characters in a sentence ?

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

#Exercise 5: Longest word without a specific character Instructions
longest_sentence = ""
while True : 
    sentence = input('Enter a sentence: ')
    if "a" in sentence.lower() :
        print("try again")
        
    elif len(sentence) > len(longest_sentence) :
        longest_sentence = sentence
        print("congratulations")
    else:
        print("Sentence not longer than the current longest. Try again!")

        
        



# Each time a user successfully sets a new longest sentence, print a congratulations message.