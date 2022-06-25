#Program objective: Given two integers a and b, find their least common multiple

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

def lcd(c, d):
    int1 = int(c / gcd(c, d))
    int2 = d
    return int1 * int2

#tests 
print(lcd(6, 8))
print(lcd(761457, 614573))
print(lcd(373, 51))