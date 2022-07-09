#Program objective: Compose the largest number out of a set of integers

def IsGreaterOrEqual(digit, maxDigit):
    int1 = [int(a) for a in str(digit)]
    int2 = [int(b) for b in str(maxDigit)]

    maxlen = max(len(int1), len(int2))
    if len(int1) > len(int2):
        i = len(int1) - len(int2)
        while i > 0:
            int2.append(int2[len(int2) - 1])
            i = i - 1
    elif len(int1) < len(int2):
        i = len(int2) - len(int1)
        while i > 0:
            int1.append(int1[len(int1) - 1])
            i = i - 1

    i = 0
    while i < len(int1):
        if int1[i] > int2[i]:
            return True
        elif int1[i] < int2[i]:
            return False
        else:
            i = i + 1

    

def maxsalary(digits):
    answer = ""
    while len(digits) > 0:
        maxDigit = 0
        for digit in digits:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        answer = answer + str(maxDigit)
        del digits[digits.index(maxDigit)]
    return answer

#tests
print(maxsalary([3, 4, 6, 9, 6]))
print(maxsalary([21, 2]))
print(maxsalary([23, 39, 92]))
print(maxsalary([1, 1, 1, 1]))
print(maxsalary([10, 11, 12, 21, 211]))