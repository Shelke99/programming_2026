def stock(prices):
    MaxProfit = 0
    sz = len(prices)
    mn = prices[0]
    for i in range(1, sz):
        MaxProfit = max(MaxProfit,prices[i]- mn)

        mn = min(mn, prices[i]) 
    return MaxProfit
print(stock([7,1,3,6,4]))
