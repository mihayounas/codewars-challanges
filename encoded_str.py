def duplicate_encode(word):
    char_count = {}
    for char in word.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    encoded_string = ""
    for char in word.lower():
        if char_count[char] > 1:
            encoded_string += ")"
        else:
            encoded_string += "("
    return encoded_string
