#Program objective: Given an integer n, find the last digit of the sum F(0) + F(1) + ... + F(n)

def fibnum(n):
    fibonacci = [0] * (n + 2)
    fibonacci[0] = 0
    fibonacci[1] = 1
    if n > 1:
        i = 2
        while i <= n: 
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
            i = i + 1
    return fibonacci[n]

def pisanolen(m):
    length = 2
    while not(fibnum(length) % m == 0 and fibnum(length + 1) % m == 1):
        length = length + 1
    return length 

def fibonaccimodmain(n, m):
    remainder = n % pisanolen(m)
    return fibnum(remainder) % m

def lastdigitfibsum(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + fibonaccimodmain(i, 10)
        i = i + 1
    return sum % 10

#tests
print(lastdigitfibsum(3))
print(lastdigitfibsum(100))
print(lastdigitfibsum(1))
print(lastdigitfibsum(0))