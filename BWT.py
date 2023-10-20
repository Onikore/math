def encode(text):
    arr = []
    for i in range(len(text)):
        arr.append((text[i:] + text[:i], i == 0))
    last_char = []
    arr = sorted(arr)
    code_num = 0
    for i in range(len(arr)):
        last_char.append(arr[i][0][-1])

        if arr[i][1]:
            code_num = i + 1
    return bytearray(last_char), code_num


def decode():
    pass
