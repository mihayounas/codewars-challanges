def sum_strings(x, y):
    result = []
    carry = 0
    i, j = len(x) - 1, len(y) - 1

    while i >= 0 or j >= 0 or carry:
        digit_x = int(x[i]) if i >= 0 else 0
        digit_y = int(y[j]) if j >= 0 else 0
        digit_sum = digit_x + digit_y + carry

        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

        i = i - 1 if i >= 0 else i
        j = j - 1 if j >= 0 else j

    # Reverse the result and remove leading zeros
    result = ''.join(result[::-1]).lstrip('0')

    # Return '0' if the result is empty (all zeros)
    return result if result else '0'
