class Solution(object):
    def longestPalindromicSubstring(self, s):
        # init result for substring and max_substring_length 
        result = ""
        max_substring_length = 0

        # loop through string s 
        for i in range(len(s)):
            # case for odd length string
            # init pointers 
            left, right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > max_substring_length:
                    result = s[left:right + 1]                          # set result to substring 
                    max_substring_length = (right - left + 1)           # update max_substring_length

                # increment/decrement pointers
                left -= 1
                right += 1

            # case for even length string 
            left, right = i, i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1) > max_substring_length:
                    result = s[left:right+1]                            # set result to substring 
                    max_substring_length = (right - left + 1)           # update max_substring_length

                # increment/decrement pointers 
                left -= 1
                right += 1
        return result 
