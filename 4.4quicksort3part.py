#Program objective: force the given implementation of the quick sort algorithm to 
#efficiently process sequences with few unique elements using a 3-way partition

import random

def partition3(a, l, r):
    j = l
    k = l
    i = l + 1
    while i < r + 1:
        if a[i] < a[l]:
            j += 1
            k += 1
            a[i], a[k] = a[k], a[i]
            a[k], a[j] = a[j], a[k]
        elif a[i] == a[l]:
            k = i
            a[i], a[k] = a[k], a[i]
        i = i + 1
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)
    return a

def quicksort3(a):
    return randomized_quick_sort(a, 0, len(a) - 1)

#tests
print(quicksort3([2, 3, 9, 2, 2]))
print(quicksort3([1, 3, 9, 5, 2, 5, 9]))
print(quicksort3([2, 3, 9, 2, 4, 2, 9, 3]))
print(quicksort3([1, 2, 3, 4, 5]))
