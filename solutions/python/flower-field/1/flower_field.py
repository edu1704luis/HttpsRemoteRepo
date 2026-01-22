def annotate(garden):
    """
    Annotate a garden grid by counting adjacent flowers for each empty space.

    :param garden: List of strings representing the garden ('*' for flowers, ' ' for empty soil).
    :return: List of strings where empty spaces show the count of neighboring flowers.
    """
    if not garden:
        return []
    allowed = {"*"," "}
    number_rows = len(garden)
    number_colums = len(garden[0])
    for act in range(0,number_rows):
        if (number_colums != len(garden[act])) or not set(garden[act]).issubset(allowed):
            raise ValueError("The board is invalid with current input.")
    r = 0
    c = 0
    temp_out = ""
    output = []
    maping =[(-1,-1), (-1,0), (-1,1),
         (0,-1),          (0,1),
         (1,-1), (1,0), (1,1)]
    for r in range(number_rows):
        for c in range(number_colums):
            if garden[r][c] == " ":
                flowers =0
                for dr, dc in maping:
                    new_row = r + dr
                    new_column = c + dc
                    if 0 <= new_row < number_rows and 0 <= new_column < number_colums:
                        if garden[new_row][new_column] == "*":
                            flowers +=1
                if flowers == 0:
                    temp_out += " "
                else:
                    temp_out += str(flowers)
            else:
                temp_out += "*"
        output.append(temp_out)
        temp_out = ""
    return output
