import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to return the definition of a word
def get_definition(dictionary, word):
    word = word.lower()  # Convert word to lowercase for case-insensitive search
    if word in dictionary:
        return dictionary[word]
    else:
        # Use difflib to suggest similar words
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.8)
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found in the dictionary."

# Main function
def main():
    dictionary = load_dictionary('./dictionary-data/data.json')

    while True:
        word = input("Enter a word to get its definition (or 'q' to quit): ")
        if word.lower() == 'q':
            break

        definition = get_definition(dictionary, word)
        print(definition)

if __name__ == "__main__":
    main()



''' 
    # class A:
    #     def __init__(self, num):
    #         self.num = num  # Corrected the initialization of num
        
    #     def change(self):
    #         self.num = 7

    # a = A(5)
    # print(a.num)

    # a.change()
    # print(a.num)

'''