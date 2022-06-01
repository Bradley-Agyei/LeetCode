class Solution(object):
    def houseRobber(self, nums):
        # init rob1, rob2 
        rob1, rob2 = 0,0 

        # loop through nums
        for n in nums:
            # store max in temp
            temp = max(rob1 + n, rob2)
            # set rob1 to rob2
            rob1 = rob2
            # set rob2 to temp
            rob2 = temp
        return rob2 