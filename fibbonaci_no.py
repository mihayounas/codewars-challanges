def productFib(prod):
    # Calculate Fibonacci numbers until the product of two consecutive numbers is greater than or equal to prod
    fib = [0, 1]
    while fib[-1] * fib[-2] < prod:
        fib.append(fib[-1] + fib[-2])
    
    # Check if the product of the last two Fibonacci numbers is equal to, less than, or greater than prod
    if fib[-1] * fib[-2] == prod:
        return [fib[-2], fib[-1], True]
    elif fib[-1] * fib[-2] < prod:
        return [fib[-1], fib[-2], False]
    else:
        return [fib[-2], fib[-1], False]
