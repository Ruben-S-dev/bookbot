from stats import count_words
from stats import count_char
from stats import sorted_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read() # returns the entire booktext as a string
    return file_contents  

def main():
    file_contents = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    wordcount = f"Found {count_words(file_contents)} total words"
    print(wordcount)
    charcount = count_char(file_contents)
    sorted_chars = sorted_report(charcount)
    for char in sorted_chars:
        print(f"{char[0]}: {char[1]}")
    print("============ END ============")
main()