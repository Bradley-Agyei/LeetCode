class Solution(object):
    def productOfArrayExceptSelf(self, nums):
        # find length of nums and init result array with length 
        length = len(nums)
        result = [0] * length 

        # init 0th index of result to 1
        result[0] = 1 

        # loop through nums from left -> right and store product in result
        for i in range(1, length):
            result[i] = nums[i - 1] * result[i - 1]
        
        # init right to 1 
        right = 1

        # loop through nums from right to left and calculate product 
        for i in reversed(range(length)):
            result[i] = result[i] * right
            right *= nums[i]
        return result

#Time comp: O(n)
#Space comp: O(1)

