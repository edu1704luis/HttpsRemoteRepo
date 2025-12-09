def is_paired(input_string):
    """paired brackets.

    :param input_string: str - string input.
    :return: bool - Falseor true if brackets are paired.
    """
    open_brackets = ["[", "{", "("]
    brackets = {"]" : "[", "}":"{", ")":"("}
    new_list = []
    for value in input_string:
        if value in open_brackets:
            new_list.append(value)
        if value in brackets and new_list != []:
            print(value, brackets[value], new_list)
            if brackets[value] == new_list[-1]:
                new_list.pop()
            else: return False
        elif value in brackets and  new_list == []:
            return False
    if new_list == []:
        return True
    return False