#Program objective: Implement the algorithm for computing the edit distance between two strings

def editdistance(string1, string2):
    A = [char for char in string1]
    B = [char for char in string2]
    A.insert(0, '0')
    B.insert(0, '0')
    
    n = len(A)
    m = len(B)
    D = [[0 for x in range(m)] for y in range(n)]
    for i in range(1, n):
        D[i][0] = i 
    for j in range(1, m):
        D[0][j] = j

    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if A[i] == B[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[n - 1][m - 1]

#tests
print(editdistance('abc', 'abc'))
print(editdistance('short', 'ports'))
print(editdistance('editing', 'distance'))
print(editdistance('bread', 'really'))