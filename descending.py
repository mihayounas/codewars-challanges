def descending_order(num):
    digits = [int(d) for d in str(num)]
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))