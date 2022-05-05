class Solution(object):
    def longestSubWithoutRepeatChar(self, s):
        # init length of s, hashmap, pointer and longest_sub 
        length = len(s)
        hashmap = {}
        longest_sub = 0
        i = 0 

        # loop through s 
        for j in range(length):

            # condition: if current char is already in map 
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)

            # if not in map, append to map and increment pointer
            longest_sub = max(longest_sub, j - i + 1)
            hashmap[s[j]] = j + 1 

        # return longest_sub
        return longest_sub 

#Time comp: O(n)
#Space comp: O(n)