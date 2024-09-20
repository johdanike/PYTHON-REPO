def split_pairs(text):
    if len(text) % 2 == 0:
        result = [text[i:i+2] for i in range(0, len(text), 2)]
    else:
        result = [text[i:i+2] for i in range(0, len(text), 2)]
        result[-1]+="_"
    return result


value = split_pairs('abcde')
print(value)