#Program objective: Given am integer money, compute the minimum number of 
#coins with denominations 1, 3, 4 that changes money

def moneychange(money, coins):
    MinNumCoins = [0] * (money + 1)
    for m in range(1, money + 1):
        MinNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

#tests
print(moneychange(2, [1, 3, 4]))
print(moneychange(34, [1, 3, 4]))
print(moneychange(32, [1, 8, 20]))
print(moneychange(99, [1, 11, 22, 33, 44]))