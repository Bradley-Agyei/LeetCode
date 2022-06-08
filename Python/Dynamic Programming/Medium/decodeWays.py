class Solution(object):
    def numDecodings(self, s):
        # init dp array for caching 
        dp = { len(s) : 1 }

        # recursive function to help us count number of ways 
        def countDecodings(i): 
            # case if i has already been cached in dp or last char in s
            if i in dp:
                return dp[i]
            
            # case if char is 0 
            if s[i] == "0":
                return 0

            # set result to recursive function + 1
            result = countDecodings(i + 1)
            # check double digits 
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456")):
                result += countDecodings(i+2)
            dp[i] = result 
            return result

        return countDecodings(0)

# Time comp: O(n)
# Space comp: O(n)