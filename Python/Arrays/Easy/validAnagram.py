class Solution(object):
    def validAnagram(self, s, t):
        # sort s and t  
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))

        # compare length of s to t: if != then return False
        if len(s) != len(t):
            return False

        # if sortedS == sortedT return True 
        if sortedS == sortedT:
            return True 
        return False 

#Time comp: O(nlogn) - Sorting 
#Space comp: O(1)

        