class Solution(object):
    def maximumSubarray(self, nums):
        # init 2 variables to the first element of nums 
        current_subarray = final_sum = nums[0]

        # case where there's only 1 element in nums
        if len(nums) == 1:
            return nums[0]
            
        # loop through nums starting from 2nd element and update current_subarray and final_sum
        for i in nums[1:]:
            current_subarray = max(i, current_subarray + i)
            final_sum = max(final_sum, current_subarray)
        return final_sum 
    
    #Time comp: O(n)
    #Space comp: O(1)