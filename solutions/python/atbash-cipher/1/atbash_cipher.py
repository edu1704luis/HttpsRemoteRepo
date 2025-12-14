def encode(plain_text):
    text_cipher = ""
    accu = 0
    new_plain_text = plain_text.lower()
    for value in new_plain_text:
        if value.isalpha():
            ascci_value = ord(value)-97
            text_cipher += chr(122-ascci_value)
            accu += 1
        if value.isdigit():
            text_cipher += value
            accu += 1
        if accu == 5:
            text_cipher += " "
            accu = 0
    return text_cipher.strip()


def decode(ciphered_text):
    text_plain = ""
    for value in ciphered_text:
        if value.isalpha():
            ascci_value = ord(value)-97
            text_plain += chr(122-ascci_value)
        if value.isdigit():
            text_plain += value
    return text_plain
