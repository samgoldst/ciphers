alphabet = list("abcdefghijklmnopqrstuvwxyz")

def find(letter):
    for index, char in enumerate(alphabet):
        if letter == char:
            return index
    return None


def caesar_cipher_encrypt(message, shift):
    output = ''
    shift_num = find(shift)
    for char in message:
        if find(char) is None:
            output += char
        else:
            output += alphabet[(find(char) + shift_num) % len(alphabet)]
    return output

def caesar_cipher_decrypt(message, key):
    output = ''
    shift_num = find(key)
    for char in message:
        if find(char) is None:
            output += char
        else:
            output += alphabet[(find(char) - shift_num) % len(alphabet)]
    return output


def vignere_cipher_encrypt(message, key):
    output = ''
    for index, char in enumerate(message):
        if find(char) is None:
            output += char
        else:
            shift_num = find(key[index % len(key)])
            output += alphabet[(find(char) + shift_num) % len(alphabet)]
    return output

def vignere_cipher_decrypt(message, key):
    output = ''
    for index, char in enumerate(message):
        if find(char) is None:
            output += char
        else:
            shift_num = find(key[index % len(key)])
            output += alphabet[(find(char) - shift_num) % len(alphabet)]
    return output

def goldstein_cipher_encrypt(message, key):
    output = ''
    for index, char in enumerate(message):
        if find(char) is None:
            output += char
        else:
            shift_num = find(message[index - 1])
            output += alphabet[(find(char) - shift_num) % len(alphabet)]
    return output