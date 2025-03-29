def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents


def get_char_count(book_text):
  lower_case = book_text.lower()
  unique_char = {}
  for char in lower_case:
    if char != "\n" and char != " ":
      if char not in unique_char:
        unique_char[char] = 1
      elif char in unique_char:
        unique_char[char] += 1
  return unique_char


def sorted_count(char_dict):
  dict_list = []
  for char in char_dict:
    if char.isalpha() and char not in dict_list:
      append_dict = {
        'char': char,
        'num': char_dict[char]
      }
      dict_list.append(append_dict)

  def sort_on(dict):
    return dict["num"]

  dict_list.sort(reverse=True, key=sort_on)
  return dict_list



def get_num_words(book):
  words_list = book.split()
  return len(words_list)