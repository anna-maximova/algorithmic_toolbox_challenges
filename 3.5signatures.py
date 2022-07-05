#Program objective: Given a set of n segments {[a_0, b_0], [a_1, b_1], ..., [a_(n-1), b_(n-1)]}
#with integer coordiantes on a line, find the minimum number m of point such that each segment 
#contains at least one point. That is, find a set of integers X of the minimum size such that 
#for any segment [a_i, b_i] there is a point x in X such that a_i <= x <= b_i

def leastsegments(n, a, b):
    segment = []
    while n > 0:
        seg = min(b)
        segment.append(seg)
        amount = 0
        length = len(a)
        i = 0
        while i < len(a):
            if a[i] <= seg and b[i] >= seg:
                amount = amount + 1
                del a[i]
                del b[i]
            else:
                i = i + 1
        n = n - amount
    return segment

#tests
print(leastsegments(3, [1, 2, 3], [3, 5, 6]))
print(leastsegments(4, [4, 1, 2, 5], [7, 3, 5, 6]))
print(leastsegments(12, [2, 5, 2, 21, 5, 13, 9, 9, 4, 8, 17, 8], [18, 10, 6, 23, 7, 15, 13, 21, 10, 11, 20, 17]))