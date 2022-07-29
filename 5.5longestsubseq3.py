#Program objective: Given three sequences, return the length of their longest common subsequence

def lengthCS3(A, B, C):
    A.insert(0, '0')
    B.insert(0, '0')
    C.insert(0, '0')
    n = len(A)
    m = len(B)
    p = len(C)
    M = [[[0 for z in range(p)] for x in range(m)] for y in range(n)]

    for i in range(1, n):
        M[i][0][0] = 0
    for j in range(1, m):
        M[0][j][0] = 0
    for k in range(1, p):
        M[0][0][k] = 0
    
    for k in range(1, p):
        for j in range(1, m):
            for i in range(1, n):
                if A[i] == B[j] == C[k]:
                    M[i][j][k] = M[i - 1][j - 1][k - 1] + 1
                else:
                    M[i][j][k] = max(M[i - 1][j][k], M[i][j - 1][k], M[i][j][k - 1])
    return M[n - 1][m - 1][p - 1]

print(lengthCS3([1, 2, 3], [2, 1, 3], [1, 3, 5]))
print(lengthCS3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))