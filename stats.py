def number_of_words(text): # Takes Story file and splits it into words
    split_text = text.split() # Creates a list of the split text
    number = len(split_text) # Counts items in that list and assigns it to number
    return number
    
def characters(book_text): # book_text here is Story from main.py
    character_number = {} # Empty dictionary to store key/value for later
    lowercase_text = book_text.lower() # Bound Story text to be all lowercase
    for character in lowercase_text: # Looped over lowercase_text to look for presence of characters
        if character not in character_number: # Looks for a character in the empty dictionary
            character_number[character] = 0 # If it's not present, it sets it to 0
        character_number[character] += 1 # If it is present, it increments by 1 for every count
    return character_number # Characters function returns the dictionary

def sorted_characters(entry): # The reverse .sort calls upon this function to locate what to sort by. "Entry" is the dictionary item
    return entry["number"]

def character_list(character_count): # character_count is dictionary character_number up above ^ it is a character and its amount
    sorted_dictionary = [] # Created a list to be able to sort because diciontaries aren't sortable. I should have named this sorted_list
    for characters, numbers in character_count.items(): # We locally renamed the keys in character count .items to be characters and numbers
        sorted_dictionary.append({"character": characters, "number": numbers}) # We append the dictionary to add labels to the keys
    sorted_dictionary.sort(reverse=True, key=sorted_characters) # This sorts the now filled list in descending order by the key - number
    return sorted_dictionary