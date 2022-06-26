#Program objective: Given an integer n, find the nth Fibonacci number F(n)

def Fibnum(n):
    fibonacci = [0] * (n + 2)
    fibonacci[0] = 0
    fibonacci[1] = 1
    if n > 1:
        i = 2
        while i <= n: 
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
            i = i + 1
    return fibonacci[n]

#Print the first 20 prime numbers
i = 1
while i <= 20:
    print(Fibnum(i))
    i = i + 1
