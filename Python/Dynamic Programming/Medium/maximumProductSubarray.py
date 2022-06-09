class Solution(object):
    def maxSub(self, nums):
        # init result to max(nums), current_max, current_min
        result = max(nums)
        current_max, current_min = 1, 1

        # loop through nums
        for n in nums:
            # use temp var to store current_max 
            temp = current_max * n
            
            current_max = max(current_max * n, current_min * n, n)
            current_min = min(temp, current_min * n, n)
            result = max(result, current_max)

        return result 