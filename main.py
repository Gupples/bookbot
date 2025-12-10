# Takes a filepath as input and returns the contents of the file as a string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return None

# Use get_book_text with the relative bpath to a file to print the contents of the book to the console.
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

if __name__ == "__main__":
    main()