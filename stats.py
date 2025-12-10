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

