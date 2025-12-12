def words_counter(text_book):
    words_in_book = text_book.split()
    return len(words_in_book)


def char_counter(text_book):
    count = {}
    for char in text_book:
        c = char.lower()
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count


def sorted_char_counter(chars_dict):
    list_dict = []

    for elem in chars_dict:
        new_dict = {"char": elem, "num": chars_dict[elem]}
        list_dict.append(new_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


def sort_on(items):
    return items["num"]
