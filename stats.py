'''
COUNT BOOK WORDS
Splits the contents of a book and returns the number of words it contains
Inputs:
    contents - the contents of a book as a string
Returns:
    The length of contents.split()
'''
def count_book_words(contents):
    word_list = contents.split()
    return len(word_list)

'''
COUNT BOOK CHARACTERS
Count the number of times each character (including symbols and spaces) appears in the book.
Inputs:
    contents - the contents of a book as a string
Returns:
    characters - A dictionary {character(string): count(int)} of each 
        character's occurance
'''
def count_book_characters(contents):
    characters = {}
    for char in contents:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

'''
SORT_DICTIONARY
Sorts a dictionary by character count
Inputs:
    characters - A dictionary {character(string): count(int)} of each 
        character's occurance
Returns:
    characters - A dictionary {character(string): count(int)} of each 
        character's occurance, sorted by each character's count
'''
def sort_dictionary(characters):
    
    # Helper function to use for sorting.
    def sort_on(items):
        return items["num"]
    
    