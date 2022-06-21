#Program objective: Given two integers a and b, find their greatest common divisor

def gcd(a, b):
    integers = [a, b]
    int1 = max(integers)
    int2 = min(integers)

    remainder = 1
    while remainder != 0:
        remainder = int1 % int2
        int1 = int2
        int2 = remainder
    return int1

#tests
print(gcd(35, 18))
print(gcd(3, 6))
print(gcd(2948957, 849374))
print(gcd(28851538, 1183019))