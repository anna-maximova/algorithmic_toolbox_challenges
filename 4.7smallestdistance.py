#Program objective: Given n points on a plane, find the smallest distance 
#between a pair of two different points

import math

def smallestdist(points):
    return mindistance(points)[1]

def mindistance(points):
    d = distance(points[0], points[1])
    if len(points) == 2:
        return [points, d]
    elif len(points) == 3:
        d = min(distance(points[0], points[1]), distance(points[0], points[2]), distance(points[1], points[2]))
        return [points, d]
    S1 = split(points)[0]
    S2 = split(points)[1]
    d1 = mindistance(S1)[1]
    d2 = mindistance(S2)[1]
    d = min(d1, d2)
    
    if len(S1) == len(S2):
        m = (S1[len(S1) - 1][1] + S2[0][1]) / 2
    else:
        m = S2[0][0]

    for i in S1:
        if i[0] < m - d:
            del S1[S1.index(i)]
    for i in S2:
        if i[0] > m + d:
            del S2[S2.index(i)]
    
    for i in S1:
        for j in S2:
            if distance(i, j) < d:
                d = distance(i, j)

    return points, d

def split(points):
    A = mergesort(points)
    m = math.ceil(len(A) / 2)
    S1 = A[:m]
    S2 = A[m:]
    return S1, S2 

def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def mergesort(A):
    if len(A) == 1:
        return A
    m = math.floor(len(A) / 2)
    B = mergesort(A[:m])
    C = mergesort(A[m:])
    A = merge(B, C)
    return A

def merge(B,C):
    D = []
    while len(B) > 0 or len(C) > 0:
        if len(B) == 0:
            D.append(C[0])
            del C[0]
        elif len(C) == 0:
            D.append(B[0])
            del B[0]
        else: 
            b = B[0][0]
            c = C[0][0]
            if b <= c:
                D.append(B[0])
                del B[0]
            else:
                D.append(C[0])
                del C[0]
    return D

#tests
print(smallestdist([[0,0], [3, 4]]))
print(smallestdist([[7, 7], [1, 100], [4, 8], [7, 7]]))
print(smallestdist([[4, 4], [-2, -2], [-3, -4], [-1, 3], [2, 3], [-4, 0], [1, 1], [-1, -1], [3, -1], [-4, 2], [-2, 4]]))