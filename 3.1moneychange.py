#Program objective: Find the minimum number of coins needed to change the input value 
#(an integer) into coins with denominations 1, 5, 10

def moneychange(total):
    numberofcoins = 0
    while total > 0:
        if total >= 10:
            total = total - 10
        elif total >= 5:
            total = total - 5
        else:
            total = total - 1
        numberofcoins = numberofcoins + 1
    return numberofcoins

#tests
print(moneychange(2))
print(moneychange(28))
print(moneychange(0))
print(moneychange(284))
print(moneychange(5))