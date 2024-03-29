#Program objective: Compute the last digit of F(0)^2 + F(1)^2 + ... + F(n)^2

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

def lastdigitsquaressum(n):
    int1 = fibonaccimodmain(n, 10)
    int2 = fibonaccimodmain(n + 1, 10)
    return (int1 * int2) % 10

#tests
print(lastdigitsquaressum(7))
print(lastdigitsquaressum(73))
print(lastdigitsquaressum(1234567890))
print(lastdigitsquaressum(0))