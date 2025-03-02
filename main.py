from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        # f is a file object
        return f.read()



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]


    text = get_book_text(path)
    
    num_words = count_words(text)
    char_counts = count_all_character(text)
    #print(f"{num_words} words found in the document")
    
    sorted_char_list = sort_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_char_list:
        print(f"{entry['character']}: {entry['count']}")

    print("============= END ===============")

main()
    