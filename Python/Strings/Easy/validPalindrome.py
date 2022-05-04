class Solution(object):
    def validPalindrome(self, s):
        # init pointers, length of s
        length = len(s)
        left, right = 0, length - 1

        # condition to stay in range 
        while left < right:

            # condition to check if pointers are alnum
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # check if pointers equal each other - if not return false
            if s[left].lower() != s[right].lower():
                return False 
        # update pointers 
            left += 1
            right -= 1

        # return True 
        return True 
        
#Time comp: O(n)
#Space comp: O(1)