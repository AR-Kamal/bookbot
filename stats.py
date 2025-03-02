def count_words(text):
 
    words_in_file = text.split()

    return len(words_in_file)


def count_all_character(text):
    lower_case = text.lower()
    char_dict = {}
    for char in lower_case:
        char_dict[char] = char_dict.get(char, 0) + 1
        
    return char_dict

def sort_character_counts(char_dict):
    sorted_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return [{"character": char, "count": count} for char, count in sorted_list]


