import collections
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        # store ans using defaultdict
        result = collections.defaultdict(list)

        # loop through strings 
        for s in strs:
            # list to store the count 
            count = [0] * 26

            # loop through individual chars in strings and update count 
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()

#Time comp: O(NK) where N is length of strs and K is max length of a string in strs
#Space comp: O(NK) total info stored in result 

