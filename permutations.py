def permutations(s):
    # Base case: If the string has only one character, return it as a single-item list
    if len(s) == 1:
        return [s]

    # Recursive case: Generate permutations by selecting each character as the first character
    # and recursively permuting the remaining characters
    result = []
    for i in range(len(s)):
        # Select the i-th character as the first character
        first_char = s[i]

        # Generate permutations of the remaining characters
        remaining_chars = s[:i] + s[i+1:]
        sub_permutations = permutations(remaining_chars)

        # Add the first character to each permutation of the remaining characters
        for perm in sub_permutations:
            result.append(first_char + perm)

    return result
