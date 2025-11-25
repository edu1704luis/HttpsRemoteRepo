def label(colors):
    """ calculate code colors resistors 3 band

    :param colors: lsit[str] - list strings colors bands 
    :return: str - value code colors
    """
    code_base_colors=['black', 'brown', 'red',
                     'orange', 'yellow', 'green',
                     'blue', 'violet', 'grey', 'white']
    result = 0
    result += code_base_colors.index(colors[0])*10
    result += code_base_colors.index(colors[1])
    result *= 10**code_base_colors.index(colors[2])
    if result >= 1_000_000_000:
        value = result/1_000_000_000
        unit = "gigaohms"
    elif result >= 1_000_000:
        value = result/1_000_000
        unit ="megaohms"
    elif result >= 1_000:
        value = result/1_000
        unit ="kiloohms"
    else:
        value = result
        unit = "ohms"
    if value == int(value): value = int(value)
    return f"{value} {unit}"

