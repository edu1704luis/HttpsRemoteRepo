def find_anagrams(word, candidates):
    output = []
    list_word = list(word.lower())
    list_word.sort()
    for option in candidates:
        list_option = list(option.lower())
        list_option.sort()
        if list_word == list_option:
            if not(word.lower() == option.lower()):
                output.append(option)
    return output