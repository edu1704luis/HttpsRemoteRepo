def resistor_label(colors):
    """ calculate code colors resistors 4-5 band

    :param colors: lsit[str] - list strings colors bands 
    :return: str - value code colors
    """
    code_base_colors = ['black', 'brown', 'red',
                     'orange', 'yellow', 'green',
                     'blue', 'violet', 'grey', 'white']
    tolerance = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25,
                 'green': 0.5,  'brown': 1, 'red': 2,
                 'gold': 5, 'silver': 10}
    result = 0
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    elif len(colors) == 5:
        result += code_base_colors.index(colors[0])*100
        result += code_base_colors.index(colors[1])*10
        result += code_base_colors.index(colors[2])
    else:
        result += code_base_colors.index(colors[0])*10
        result += code_base_colors.index(colors[1])
    result *= 10**code_base_colors.index(colors[-2])
    tol = tolerance[colors[-1]]
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
    return f"{value} {unit} ±{tol}%"
