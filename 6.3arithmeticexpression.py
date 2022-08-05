#Program objective: Find the maximum value of an arithmetic expression by specifying
#the order of applying its arithmetic operations using additional parentheses

import numpy as np

def maxarithmetic(expression):
    expressionparsed = expression.split(' ')
    values = []
    operators = []
    i = 0
    while i < len(expressionparsed):
        if i % 2 == 0:
            values.append(expressionparsed[i])
        else:
            operators.append(expressionparsed[i])
        i += 1
    
    n = len(values)

    M = np.zeros((n, n))
    m = np.zeros((n, n))

    for i in range(n):
        M[i, i] = values[i]
        m[i, i] = values[i]

    for difference in range(1, n):
        for i in range(n - difference):
            j = i + difference
            m[i, j], M[i, j] = MinandMax(i, j, operators, M, m)
    return M[0, n - 1]

def MinandMax(i, j, operators, M, m):
    maximum = float('-inf')
    minimum = float('inf')
    for k in range(i, j):
        a = calculate(M[i, k], operators[k], M[k + 1, j])
        b = calculate(M[i, k], operators[k], m[k + 1, j])
        c = calculate(m[i, k], operators[k], M[k + 1, j])
        d = calculate(m[i, k], operators[k], m[k + 1, j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def calculate(int1, op, int2):
    if op == '+':
        result = int1 + int2
    elif op == '-':
        result = int1 - int2
    elif op == '*':
        result = int1 * int2
    return result

#tests 
print(maxarithmetic("1 + 5"))
print(maxarithmetic("5 - 8 + 7 * 4 - 8 + 9"))