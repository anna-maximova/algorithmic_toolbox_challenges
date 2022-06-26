#Program objective: Given two non-negative integers m and n, where m <= n, find the last digit of the sum 
#F(m) + F(m+1) + ... + F(n)

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

def lastdigitpartialsum(m, n):
    sum = 0
    i = m
    while i <= n:
        sum = sum + fibonaccimodmain(i, 10)
        i = i + 1
    return sum % 10

#tests
print(lastdigitpartialsum(3, 7))
print(lastdigitpartialsum(10, 10))
print(lastdigitpartialsum(10, 200))
print(lastdigitpartialsum(1, 2))
print(lastdigitpartialsum(0, 1))
print(lastdigitpartialsum(0, 0))
