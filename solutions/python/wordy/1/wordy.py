def operations(operation: str, arg1: int, arg2: int) -> int:
    """Operation with two args.

    :param operation: str - operation type.
    :param arg1: int - number arg1.
    :param arg2: int - number arg2.
    :return: int - Operation result
    """
    if operation == "plus":
        return arg1 + arg2
    elif operation == "minus":
        return arg1 - arg2
    elif operation == "multiplied":
        return arg1 * arg2
    elif operation == "divided":
        return arg1 / arg2


def answer(question: str):
    """Given an operation in string format, it evaluates it
    and obtains the result.

    :param question: str - operation in string format.
    :return: int - Operation result
    """
    new_question = question.removesuffix("?")
    question_list = new_question.split(" ")
    operations_list = ["plus", "minus", "multiplied", "divided"]
    number_list = []
    op_list = []
    accu_num = []
    if question_list[0] == "What" and question_list[1] == "is":
        for index, value in enumerate(question_list[2:len(question_list)]):
            if value.isnumeric():
                number_list.append(int(value))
                accu_num.append(index)
            elif value.startswith("-") and value[1:].isnumeric():
                number_list.append(int(value))
                accu_num.append(index)
            elif value in operations_list:
                op_list.append(value)
            elif value != "by":
                raise ValueError("unknown operation")
        accu = 0
        for val in accu_num:
            if abs(val - accu) == 1:
                raise ValueError("syntax error")
            accu = val
        if len(number_list) == 1 and len(op_list) == 0:
            return number_list[0]
        if len(number_list)-1 != len(op_list) or (number_list is op_list):
            raise ValueError("syntax error")
        accu_result = number_list[0]
        for index, operator in enumerate(op_list):
            next_number = number_list[index+1]
            accu_result = operations(operator, accu_result, next_number)
        return int(accu_result)
    else:
        raise ValueError("syntax error")