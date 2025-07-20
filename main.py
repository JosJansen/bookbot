from stats import get_num_words, get_num_characters, sort_characters
import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    sorted_num_char = sort_characters(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_num_char:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
   


def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()