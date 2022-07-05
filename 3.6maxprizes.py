#Program objective: Represent a given positive integer n as a sum of as many pairwise 
#distinct positive integers as possible. That is, to find the maximum k such that n 
#can be written as a_1 + a_2 + ... + a_k where a_1, ..., a_k are positive integers and 
#a_i =/= a_j for all 1 <= i < j <= k

def maxprizes(n):
    
    i = 1
    prizes = []
    while n >= i:
        prizes.append(i)
        n = n - i 
        i = i + 1
    if n > 0:
        prizes[len(prizes) - 1] = n + i - 1
    elif n == i:
        prizes[len(prizes) - 1] = 2*n
    return prizes

#tests
print(maxprizes(6))
print(maxprizes(8))
print(maxprizes(2))
print(maxprizes(382))
print(maxprizes(1))