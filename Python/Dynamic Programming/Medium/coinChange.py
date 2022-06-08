class Solution(object):
    def coinChange(self, coins, amount):
        # init dp array 
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 

        # loop from bottom up (1...amount + 1)
        for a in range(1, amount + 1):
            for c in coins:
                if (a - c >= 0):
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1 