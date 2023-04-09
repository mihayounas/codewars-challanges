def persistence(n):
    if n < 10:
        return 0
    
    persistence_count = 0
    while True:
        multiplier = 1
        while n > 0:
            digit = n % 10
            multiplier *= digit
            n //= 10
        persistence_count += 1
        if multiplier < 10:
            break
        else:
            n = multiplier
    
    return persistence_count
