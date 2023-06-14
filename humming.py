def hamming(n):
    hamming_numbers = [1]
    i = j = k = 0
# dynamic programming approach to generate Hamming numbers - 
    while len(hamming_numbers) < n:
        next_hamming = min(hamming_numbers[i] * 2, hamming_numbers[j] * 3, hamming_numbers[k] * 5)
        hamming_numbers.append(next_hamming)

        if next_hamming == hamming_numbers[i] * 2:
            i += 1
        if next_hamming == hamming_numbers[j] * 3:
            j += 1
        if next_hamming == hamming_numbers[k] * 5:
            k += 1

    return hamming_numbers[-1]
