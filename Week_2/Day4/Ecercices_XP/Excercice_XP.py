import random

# Step 1: Get words from file
def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()   # split by spaces or newlines
    return words

# Step 2: Generate random sentence
def get_random_sentence(length):
    words = get_words_from_file("words.txt")  # load words from file
    sentence = " ".join(random.choice(words) for _ in range(length))
    return sentence.lower()

# Step 3: Main function
def main():
    print("This program generates a random sentence from a list of words.")
    try:
        length_of_sentence = int(input("Enter the desired length of the sentence (2–20): "))
        
        if 2 <= length_of_sentence <= 20:
            random_sentence = get_random_sentence(length_of_sentence)
            print("Random sentence:", random_sentence)
        else:
            print("Error: Length must be between 2 and 20.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# Run the program
main()

#Excercice2:

print("\n Exercise 2: Working with JS \n")
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
print("Original JSON data:", data)
salary_value = data["company"]["employee"]["payable"]["salary"]
print("Salary value:", salary_value)
data["company"]["employee"]["birth_date"] = "1990-01-01"

with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified JSON saved to 'modified_data.json'")