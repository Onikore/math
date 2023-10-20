def encode(input_string, alphabet):
    sequence = []
    alp = alphabet.copy()
    for char in input_string:
        index = alp.index(char)
        sequence.append(index)
        alp = [alp.pop(index)] + alp
    return sequence


def decode(sequence, alphabet):
    chars = []
    alp = alphabet.copy()
    for i in sequence:
        char = alp[i]
        chars.append(char)
        alp = [alp.pop(i)] + alp
    return ''.join(chars)
