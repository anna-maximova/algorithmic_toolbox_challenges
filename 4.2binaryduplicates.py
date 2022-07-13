#Program objective: Implement binary search algorithm, given a sequence and a list of numbers return
#sequence of the first occurences of the numbers in the sequence and -1 if the number is not in the sequence

import math

def binaryfirst(sequence, number):
    i = 0
    minindex = 0
    maxindex = len(sequence) - 1
    while i < (math.ceil(math.log(len(sequence) - 1)) + 1):
        check = math.floor((maxindex - minindex) / 2) + minindex
        if number == sequence[check]:
            while number == sequence[check]:
                check = check - 1
                if check == -1:
                    return 0
            return check + 1
        elif number < sequence[check]:
            maxindex = check - 1
        else:
            minindex = check + 1
        i = i + 1
    
    if i == math.ceil(math.log(len(sequence) - 1)) + 1:
        return -1

def binarysearch(sequence, numbers):
    placearray = []
    for i in numbers:
        placearray.append(binaryfirst(sequence, i))
    return placearray

#tests
print(binarysearch([1, 5, 8, 12, 13], [8, 1, 23, 1, 11]))
print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [8, 3, 15, 9]))
print(binarysearch([2, 4, 4, 4, 7, 7, 9], [9, 4, 5, 2]))
print(binarysearch([1, 1, 1, 1, 1, 1], [2, 5, 1]))