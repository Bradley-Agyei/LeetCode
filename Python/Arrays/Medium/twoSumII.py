class Solution(object):
    def twoSumII(self, nums, target):
        # init length, left and right pointer
        length = len(nums)
        left, right = 0, length - 1  

        # ensure in bounds (while)
        while (left < right):
            # init sum 
            sum = nums[left] + nums[right]

            # condition: if sum == target
            if sum == target:
                return left + 1, right + 1

            # condition: if sum < target
            elif (sum < target):
                left += 1
            
            # condition: if sum > target 
            else: 
                right -= 1 


