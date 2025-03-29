import sys
from stats import *

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_string = get_book_text(sys.argv[1])
    num_words = get_num_words(book_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    to_sort = get_char_count(book_string)
    sorted_chars = sorted_count(to_sort)
    for char in sorted_chars:
      print(f"{char["char"]}: {char["num"]}")

main()