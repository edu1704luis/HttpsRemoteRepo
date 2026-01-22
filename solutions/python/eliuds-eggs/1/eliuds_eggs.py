def egg_count(display_value):
    new=bin(display_value)
    list_bits = str(new)
    list_bits = list_bits[2:]
    return list_bits.count("1")
