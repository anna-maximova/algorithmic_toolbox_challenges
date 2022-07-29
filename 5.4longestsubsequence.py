#Program objective: Given two sequences, return the length of their longest common subsequence

def lengthCS(A, B):
    A.insert(0, '0')
    B.insert(0, '0')
    n = len(A)
    m = len(B)
    M = [[0 for x in range(m)] for y in range(n)]

    for i in range(1, n):
        M[i][0] = 0
    for j in range(1, m):
        M[0][j] = 0
    
    for j in range(1, m):
        for i in range(1, n):
            if A[i] == B[j]:
                M[i][j] = M[i - 1][j - 1] + 1
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])
    return M[n - 1][m - 1]

#tests
print(lengthCS([2, 7, 5], [2, 5]))
print(lengthCS([7], [1, 2, 3, 4]))
print(lengthCS([2, 7, 8, 3], [5, 2, 8, 7]))