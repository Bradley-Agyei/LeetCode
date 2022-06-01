class Solution(object):
    def climbingStairs(self, n):
        # init one_step, two_step
        one_step, two_step = 1, 1

        # loop through n - 1
        for i in range(n - 1):
            # put current one in temp 
            temp = one_step
            # set one to one + two
            one_step = one_step + two_step
            # shift two to previous one using temp
            two_step = temp

        return one_step 

# Time & Space comp: O(n)