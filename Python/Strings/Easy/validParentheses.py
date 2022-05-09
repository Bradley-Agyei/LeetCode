class Solution(object):
    def validParentheses(self, s):
        # init stack data structure
        stack = []

        # init mappings for valid parentheses
        mappings = {')':'(',
                    ']':'[',
                    '}':'{' }

        # loop through chars in string
        for char in s:

            # check if in mapping 
            if char in mappings:
                # if match found in mapping, pop top most element 
                top_element = stack.pop() if stack else '#'

                if mappings[char] != top_element:
                    return False 
            else:
                stack.append(char)
        return not stack 

#Time comp: O(n)
#Space comp: O(n)