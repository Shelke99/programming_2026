# Best Time to Buy and Sell Stock
def stock(prices):
    MaxProfit = 0
    sz = len(prices)
    for i in range(sz):
        for j in range(i + 1, sz):
            MaxProfit = max(MaxProfit, prices[j] - prices[i])
    return MaxProfit
print(stock([7,1,3,6,4]))