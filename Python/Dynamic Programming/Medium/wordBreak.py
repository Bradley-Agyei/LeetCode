class Solution(object):
    def wordBreak(self, wordDict, s): 
        # init dp cache and set base case 
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True 

        # loop through string s and make comparisons with w (words in wordDict) *bottom-up*
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # see if length of s is even valid to compare with w
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break 
        return dp[0]
            

