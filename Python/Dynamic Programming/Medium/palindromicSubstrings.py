class Solution(object):
    def countSubstrings(self, s):
        palindrome_count = 0
        # loop through s
        for i in range(len(s)):
            palindrome_count += self.countPalin(s, i, i)
            palindrome_count += self.countPalin(s, i, i + 1)
        return palindrome_count 

    
    # helper function to count palindromes in s
    def countPalin(self, s, left, right):
        # init palindrome_count 
        palindrome_count = 0

        while (left >= 0 and right < len(s) and s[left] == s[right]):
            palindrome_count += 1
            left -= 1
            right += 1
        return palindrome_count 