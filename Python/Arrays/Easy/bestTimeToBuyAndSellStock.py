class Solution(object):
    def bestTimeToBuyAndSellStock(self, prices):
        # init max_profit and buy_price
        max_profit = 0
        buy_price = prices[0]
        n = len(prices)

        # loop through prices to calculate max_profit and update buy_price when needed
        for i in range(n):
            if prices[i] < buy_price:
                buy_price = prices[i]
            elif (prices[i] - buy_price > max_profit):
                max_profit = prices[i] - buy_price
        return max_profit 

#Time comp: O(n)
#Space comp: O(1)