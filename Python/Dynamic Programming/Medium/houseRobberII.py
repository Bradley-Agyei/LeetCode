class Solution(object):
    def rob(self, nums):
        # initial cases: if nums is empty 
        if not nums:
            return 0 

        # condition: if nums length is 1
        if len(nums) == 1:
            return nums[0] 

        # House Robber I helper function
        def houseRobberI(nums):
            # init robber1, robber2
            robber1, robber2 = 0, 0

            # loop through nums
            for n in nums:
                # use temp var to find max
                temp = max(robber1 + n, robber2)

                # set robber1 to robber 2
                robber1 = robber2 

                # set robber 2 to temp 
                robber2 = temp

            # return robber 2
            return robber2 

         # return max using helper function 
        return max(houseRobberI(nums[1:]), houseRobberI(nums[:-1]))

# Time comp: O(n)
# Space comp: O(1)