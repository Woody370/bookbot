import sys
if len(sys.argv) != 2: # 2 because any less or more than that means the path to a book is wrong or not there
    print("Usage: python3 main.py <path_to_book>") # Prints this to tell user how to use the program
    sys.exit(1) # Errors out the program

book_path = sys.argv[1] # sys.argv is a list, and 0 is main.py, so 1 is the path_to_book. This sets book_path equal to that and then get_book_text calls it

def get_book_text(relative_filepath):
    with open(relative_filepath) as book:
        text = book.read()
        return text #text = story file

from stats import number_of_words
from stats import characters
from stats import character_list

def main():
    story = get_book_text(book_path) # Story value is now equal to the text of the story
    words = number_of_words(story)
    character_count = characters(story) # Story is now the value "book_text" in the stats.py. character_count is equal to the dictionary character_number in stats.py
    sorted_list = character_list(character_count) # The sorted, descending list from stats.py
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list: # Entry is just an item in the list
        character = entry["character"] # Sets the string character to equal the key character from the sorted list
        if not character.isalpha(): # If the string character isn't alphabetic, continue skips it
            continue
        print(f"{character}: {entry['number']}") # Prints the f-string so that the letter/integers come through on a print
    print("============= END ===============")
    
main()