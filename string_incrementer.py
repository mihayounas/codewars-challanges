def increment_string(strng):
    # Check if the string is empty
    if not strng:
        return '1'

    # Find the index where the numeric part begins
    i = len(strng) - 1
    while i >= 0 and strng[i].isdigit():
        i -= 1
    index = i + 1

    # Extract the non-numeric and numeric parts of the string
    non_numeric_part = strng[:index]
    numeric_part = strng[index:]

    if numeric_part:
        # Increment the numeric part
        new_numeric_part = str(int(numeric_part) + 1)
        # Pad with leading zeros if necessary
        if len(new_numeric_part) < len(numeric_part):
            new_numeric_part = numeric_part[0] + new_numeric_part.zfill(len(numeric_part) - 1)
    else:
        new_numeric_part = '1'

    return non_numeric_part + new_numeric_part
