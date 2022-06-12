class Solution(object):
    def decodeString(self, s):
        # init stack, length of s
        stack = []
        length_of_s = len(s)

        # loop through s 
        for i in range(length_of_s):
            # condition -> keep appending to stack while we dont see a closing bracket
            if s[i] != "]":
                stack.append(s[i])
            # condition -> seen closing bracket
            else:
                # init substring 
                substring = ""
                # keep popping and adding to substring until we see opening bracket
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()                             # pop opening bracket itself 

                # determine k (length of substring)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # multiply substring by k and append to stack 
                stack.append(int(k) * substring)

        # return stack joined with substrings 
        return "".join(stack)