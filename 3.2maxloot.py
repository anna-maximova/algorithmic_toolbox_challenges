#Program objective: Implement an algorithm for the fractional knapsack problem

def maxloot(numberitems, capacity, values, weights):
    i = 0
    cost = [0] * numberitems
    while i < numberitems:
        cost[i] = values[i] / weights[i]
        i = i + 1
    loot = 0
    while capacity != 0:
        index = cost.index(max(cost))
        amount = min(weights[index], capacity)
        loot = loot + (values[index] * amount / weights[index])
        capacity = capacity - amount
        del cost[index]
        del values[index]
        del weights[index]
    return loot

#tests
print(maxloot(3, 50, [60, 100, 120], [20, 50, 30]))
print(maxloot(1, 10, [500], [30]))