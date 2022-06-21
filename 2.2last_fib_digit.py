#Program objective: Given an integer n, find the last digit of the nth Fibonacci number F(n)

def lastFibdigit(n):
    fibdigit = [0] * (n + 1)
    fibdigit[0] = 0
    fibdigit[1] = 1
    if n > 1:
        i = 2
        while i <= n: 
            fibdigit[i] = fibdigit[i-1] + fibdigit[i-2]
            fibdigit[i] = fibdigit[i] % 10
            i = i + 1
    return fibdigit[n]

#tests
print(lastFibdigit(3))
print(lastFibdigit(331))
print(lastFibdigit(327305))
