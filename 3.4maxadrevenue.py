#Program objective: Given two sequences a_1, a_2, ..., a_n (a_i is the profit per click on the i-th ad)
#and b_1, b_2, ..., b_n (b_i is the average number of clicks per day of the i-th slot), we need to 
#partition them into n pairs (a_i, b_j) such that the sum of their products is maximized

def maxadrevenue(n, a, b):
    sum = 0
    while len(a) > 0 and len(b) > 0:
        sum = sum + max(a) * max(b)
        del a[a.index(max(a))]
        del b[b.index(max(b))]
    return sum

#tests
print(maxadrevenue(1, [23], [39]))
print(maxadrevenue(3, [1, 3, -5], [-2, 4, 1]))
print(maxadrevenue(5, [1, 4, -4, 3, 2], [2, -3, 4, -4, 1]))