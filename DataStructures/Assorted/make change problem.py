## Make Change

def dpMakeChange(coinValueList, amnt):
    minCoins = [0]*(amnt+1)
    for cents in range(amnt+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
    return minCoins[amnt], "Coins minimum required"

denomination = [1,5,10]
amount = 31
print dpMakeChange(denomination, amount)
