def square_root(number):
    pot=1
    while pot*pot < number:
        pot += 1
    return pot