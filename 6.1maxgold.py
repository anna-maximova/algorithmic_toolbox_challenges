#Program objective: Given n gold bars, find the maximum weight of gold that fits into a bag of capacity W

import numpy as np

def maxgold(W , goldbars):
    goldbars.insert(0,0)
    A = np.zeros((len(goldbars), W + 1))
    for i in range(1, len(goldbars)):
        for w in range(1, W + 1):
            A[i, w] = A[i - 1, w]
            if goldbars[i] <= w:
                A[i, w] = max(A[i - 1, w], A[i - 1, w - goldbars[i]] + goldbars[i])
    return A[len(goldbars) - 1, W]       

#tests
print(maxgold(10, [1, 4, 8]))
print(maxgold(20, [1, 3, 6]))
print(maxgold(15, [3, 6, 9, 14]))