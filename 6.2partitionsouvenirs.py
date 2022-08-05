#program objective: Given a list of souvenir values, return 1 if it is possible 
#to partition the souvenirs into three subsets with equal sums and 0 otherwise

import numpy as np

def partition(values):
    totalweight = sum(values)
    
    if totalweight % 3 != 0 or len(values) < 3:
        return 0

    W = int(totalweight / 3)

    values.insert(0, 0)
    matrix = np.zeros((len(values), W + 1))

    count = 0
    for i in range(1, len(values)):
        for w in range(1, W + 1):
            matrix[i, w] = matrix[i - 1, w]
            if values[i] <= w:
                matrix[i, w] = max(matrix[i - 1, w], matrix[i - 1, w - values[i]] + values[i])
            if matrix[i, w] == W:
                count += 1

    if count >= 3:
        return 1
    else:
        return 0

#tests
print(partition([3, 3, 3, 3]))
print(partition([1, 2, 3, 3]))
print(partition([40]))
print(partition([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))
print(partition([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))