#Program objective: Count the number of inversions of a given sequence

import math

def inversions(A):
    return mergesort(A)[1]

def mergesort(A):
    count = 0
    if len(A) == 1:
        return (A, count)
    m = math.floor(len(A) / 2)
    B = mergesort(A[:m])
    C = mergesort(A[m:])
    A = merge(B, C)
    return A

def merge(B,C):
    count = B[1] + C[1]
    i = 0
    while i < len(B[0]):
        j = 0
        while j < len(C[0]):
            if B[0][i] > C[0][j]:
                count = count + 1
            j += 1
        i += 1

    D = []
    while len(B[0]) > 0 or len(C[0]) > 0:
        if len(B[0]) == 0:
            D.append(C[0][0])
            del C[0][0]
        elif len(C[0]) == 0:
            D.append(B[0][0])
            del B[0][0]
        else: 
            b = B[0][0]
            c = C[0][0]
            if b <= c:
                D.append(b)
                del B[0][0]
            else:
                D.append(c)
                del C[0][0]
    return D, count

#tests
print(inversions([7, 3, 5, 2, 4, 1]))
print(inversions([2, 3, 9, 2, 9]))
print(inversions([1, 2, 3, 4, 5]))
print(inversions([5, 4, 3, 2, 1]))