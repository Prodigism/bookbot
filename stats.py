def get_word_count(word_count):
    word_total = word_count.split()
    return len(word_total)

def get_character_count(character_count):
    character_library = {}
    for characters in character_count:
        characters = characters.lower()
        if characters.isalpha():
            if characters in character_library:
                character_library[characters] += 1
            else:
                character_library[characters] = 1
    return character_library

def return_sorted_list(future_char_list):
    def call_dictionary(dict_key):
        return dict_key['value']
    char_sorted_list = []
    for char, value in future_char_list.items():
        temp_char_library = {'char': char, 'value': value}
        char_sorted_list.append(temp_char_library)
    char_sorted_list.sort(reverse=True,key=call_dictionary)
    return char_sorted_list