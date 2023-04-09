def descending_order(num):
    digits = [int(d) for d in str(num)]
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))


# other solution

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# other solution

def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')