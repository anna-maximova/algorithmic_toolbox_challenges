#Program objective: Given two integers n and m, output F(n) mod(m)

def fibnum(n):
    fibonacci = [0] * (n + 1)
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

#tests
print(fibonaccimodmain(2015, 3))
print(fibonaccimodmain(239, 1000))
print(fibonaccimodmain(2816213588, 239))
