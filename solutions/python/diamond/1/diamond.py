def rows(letter):
    cap_letter = letter.upper()
    number_rows = ord(cap_letter) - ord("A")
    if number_rows == 0: return([cap_letter])
    diamond_rows = []
    accu = 0
    space = 1
    act_letter = ord("A")
    for j in range(number_rows+1):
        if j == 0:
            row= f"{' '*number_rows + chr(act_letter) +' '*number_rows}"
            accu += 1
        else:
            row= f"{' '*(number_rows-accu)+ chr(act_letter+accu) + ' '*space + chr(act_letter+accu) + ' '*(number_rows-accu)}"
            space += 2
            accu += 1
        diamond_rows.append(row)
    full_diamond = diamond_rows + diamond_rows[:-1][::-1]
    return full_diamond