from stats import words_counter, char_counter, sorted_char_counter
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    text_content = get_book_text(book)

    print("----------- Word Count ----------")
    word_count = words_counter(text_content)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = char_counter(text_content)
    list_sorted = sorted_char_counter(char_count)
    for dic in list_sorted:
        char = dic["char"]
        count = dic["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
