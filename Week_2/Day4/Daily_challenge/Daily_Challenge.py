import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        return frequency if frequency > 0 else None

    def most_common_word(self):
        words = self.text.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        most_common = max(word_freq, key=word_freq.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        unique = [word for word, freq in word_freq.items() if freq == 1]
        return unique

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return cls(content)


class TextModification(Text):
    def remove_punctuation(self):
        non_pun = str.maketrans('', '', string.punctuation)
        return self.text.translate(non_pun)

    def remove_stop_words(self):
        stop_words = set([
            "i","me","my","myself","we","our","ours","ourselves","you","your","yours",
            "yourself","yourselves","he","him","his","himself","she","her","hers",
            "herself","it","its","itself","they","them","their","theirs","themselves",
            "what","which","who","whom","this","that","these","those","am","is",
            "are","was","were","be","been","being","have","has","had","having",
            "do","does","did","doing","a","an","the","and","but","if","or","because",
            "as","until","while","of","at","by","for","with","about","against","between",
            "into","through","during","before","after","above","below","to","from","up",
            "down","in","out","on","off","over","under","again","further","then","once",
            "here","there","when","where","why","how","all","any","both","each","few",
            "more","most","other","some","such","no","nor","not","only","own","same",
            "so","than","too","very","s","t","can","will","just","don","should","now"
        ])
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        return re.sub(r'[^A-Za-z0-9 ]+', '', self.text)

# Example usage:
if __name__ == "__main__":
    # Load text from file
    text_instance = TextModification.from_file("sample.txt")

    # Display original text
    print("Original Text:\n", text_instance.text)

    # Word frequency
    word = "example"
    freq = text_instance.word_frequency(word)
    print(f"\nFrequency of the word '{word}':", freq)

    # Most common word
    most_common = text_instance.most_common_word()
    print("\nMost common word:", most_common)

    # Unique words
    unique = text_instance.unique_words()
    print("\nUnique words:", unique)

    # Remove punctuation
    no_punct = text_instance.remove_punctuation()
    print("\nText without punctuation:\n", no_punct)

    # Remove stop words
    no_stop_words = text_instance.remove_stop_words()
    print("\nText without stop words:\n", no_stop_words)

    # Remove special characters
    no_special_chars = text_instance.remove_special_characters()
    print("\nText without special characters:\n", no_special_chars)