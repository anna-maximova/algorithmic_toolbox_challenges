#Program objective: Given distance d needed to travel and miles m your car can travel on
#a full tank and gas stations at distances stop(1), stop(2), ...., stop(n), calculate
#minimum number of refills needed to reach destination (if not possible return -1)

def carfueling(distance, miles, stops):
    stops.append(distance)
    drivecounter = miles
    stopcounter = 0
    i = 0
    while i < len(stops) - 1:
        if stops[i] <= drivecounter and stops[i+1] <= drivecounter:
            i = i + 1
        elif stops[i] <= drivecounter and stops[i+1] > drivecounter:
            stopcounter = stopcounter + 1
            drivecounter = miles + stops[i]
            i = i + 1
        else:
            return -1
    return stopcounter

#tests
print(carfueling(950, 400, [200, 375, 550, 750]))
print(carfueling(10, 3, [1, 2, 5, 9]))
print(carfueling(6, 3, [2, 3, 4]))
print(carfueling(7, 3, [1, 2, 3, 4, 5, 6]))
print(carfueling(7, 3, [1, 2, 6]))
print(carfueling(12, 3, [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]))
print(carfueling(200, 250, [2, 100, 150]))