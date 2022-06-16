#Program objective: find maximum product of two distinct numbers n sequence of non-negative integers.

def max_pairwise_product(size, sequence_string):
    i = 0
    sequence = [0]*size
    while i < size:
        sequence[i] = sequence_string.split()[i]
        i = i + 1

    max1 = max(sequence)

    index = sequence.index(max1)
    sequence.pop(index)
    max2 = max(sequence)

    return int(max1) * int(max2)

print(max_pairwise_product(7, "3 6 8 4 6 8 6"))
print(max_pairwise_product(3, "1 2 3"))
print(max_pairwise_product(10, "1 1 1 1 1 1 1 1 1 1"))
print(max_pairwise_product(2, "0 1"))
print(max_pairwise_product(5, "4 5 6 7 8"))