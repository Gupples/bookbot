from stats import count_book_words, count_book_characters, sort_dictionary
import sys

# Takes a filepath as input and returns the contents of the file as a string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return None
    
# Use get_book_text with the relative path to a file to print the contents of the book to the console.
def main():

    # The path to the book should be a part of the executed command.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    # Begin book report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Print word count
    print("----------- Word Count ----------")
    text_characters = count_book_characters(text)
    print(f"Found {count_book_words(text)} total words")
    
    # Print alphabetic character count
    print("--------- Character Count -------")
    sorted_characters = sort_dictionary(text_characters)
    for entry in sorted_characters:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    # Finish report
    print("============= END ===============")

if __name__ == "__main__":
    main()