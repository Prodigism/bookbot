import sys
from stats import get_word_count
from stats import get_character_count
from stats import return_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_data = get_book_text(sys.argv[1])
    word_count = get_word_count(book_data)
    character_count = get_character_count(book_data)
    sorted_list = return_sorted_list(character_count)
    print(f"============ BOOKBOT ============\n Analyzing book found at {sys.argv[1]}...\n", \
    "----------- Word Count ----------")
    print(f"Found {word_count} total words\n --------- Character Count -------")
    #print(f"{character_count}")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["value"]}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
    return book_contents

main()