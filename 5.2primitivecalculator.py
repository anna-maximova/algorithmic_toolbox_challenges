#Program objective: Given an integer n, compute the minimum number of 
#operations needed to obtain the number n starting from 1 where your 
#operations are: add 1, multiply by 2, and multiply by 3

def primitivecalculator(n):
    MinNumOpps = [0] * (n + 1)
    for i in range(2, n + 1):
        seq1, seq2, seq3 = float('inf'), float('inf'), float('inf')
        seq1 = MinNumOpps[i - 1] + 1
        if i % 3 == 0:
            seq2 = MinNumOpps[int(i / 3)] + 1
        elif i % 2 == 0:
            seq3 = MinNumOpps[int(i / 2)] + 1
        MinNumOpps[i] = min(seq1, seq2, seq3)
    
    intermediate = [n]
    i = n
    while i > 1:
        if i % 3 == 0 and MinNumOpps[i] - 1 == MinNumOpps[int(i / 3)]:
            i = int(i / 3)
        elif i % 2 == 0 and MinNumOpps[i] - 1 == MinNumOpps[int(i / 2)]:
            i = int(i / 2)
        else:
            i = i - 1
        intermediate.append(i)
    
    return MinNumOpps[n], intermediate

#tests
print(primitivecalculator(1))
print(primitivecalculator(4))
print(primitivecalculator(5))
print(primitivecalculator(9))
print(primitivecalculator(96234))