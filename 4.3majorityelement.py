# Program objective: Check if an input sequence has a majority element

import math

def compare(int1, int2, sequence):
    if int1 == int2:
        return int1
    else:
        if int1 == 0:
            count = 0
            for i in sequence:
                if i == int2:
                    count = count + 1
            if count > math.floor(len(sequence) / 2):
                return int2
            else:
                return 0
        elif int2 == 0:
            count = 0
            for i in sequence:
                if i == int1:
                    count = count + 1
            if count > math.floor(len(sequence) / 2):
                return int1
            else:
                return 0
        else:
            count1 = 0
            count2 = 0
            for i in sequence:
                if i == int1:
                    count1 = count1 + 1
                elif i == int2:
                    count2 = count2 + 1
            if count1 > math.floor(len(sequence) / 2):
                return int1
            elif count2 > math.floor(len(sequence) / 2):
                return int2
            else:
                return 0

def majorityelement(sequence):
    if len(sequence) == 1:
        return sequence[0]
    middleindex = math.ceil(len(sequence) / 2)
    int1 = majorityelement(sequence[:middleindex])
    int2 = majorityelement(sequence[middleindex:])
    return compare(int1, int2, sequence)    
    

#tests
print(majorityelement([2, 3, 9, 2, 2]))
print(majorityelement([1, 2, 3, 4]))
print(majorityelement([1, 2, 3, 1]))
print(majorityelement([1, 1, 1, 1, 1, 2, 1, 1]))
print(majorityelement([3, 3, 3, 3, 3, 1, 1, 1]))
print(majorityelement([1, 1, 2, 2]))
print(majorityelement([1, 2, 3, 2, 2, 2, 5]))