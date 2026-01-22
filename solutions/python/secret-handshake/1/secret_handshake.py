def commands(binary_str):
    reverse_binary = binary_str[::-1]
    actions = ["wink", "double blink", "close your eyes", "jump"]
    act = []
    for pos in range(0,4):
        if "1" == reverse_binary[pos]:
            act.append(actions[pos])
    if "1" == binary_str[0]:
        act.reverse()
    return act
