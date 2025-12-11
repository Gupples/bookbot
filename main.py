from stats import count_book_words, count_book_characters, sort_dictionary

# Takes a filepath as input and returns the contents of the file as a string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return None
    
# Use get_book_text with the relative bpath to a file to print the contents of the book to the console.
def main():
    text = get_book_text("books/frankenstein.txt")
    text_characters = count_book_characters(text)
    print(f"Found {count_book_words(text)} total words")
    print(f"TEXT CHARACTERS: \n {text_characters}")
    sorted_characters = sort_dictionary(text_characters)
    for entry in sorted_characters:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")

if __name__ == "__main__":
    main()