#Problem: Given an array of intgers, return an array of those integers squared in non-decreasing order
#Input: [-4,-1,0,3,10] output: [0,1,9,16,100]
#Approach: Two pointer

class Solution(object):
    def squaresOfSortedArray(self, nums):
        # init left and right pointer, length of nums, result list 
        n = len(nums)
        left, right = 0, n-1
        result = [0] * n 

        # iterate through array using for loop 
        for i in range(n-1,-1,-1):
            # compare value of left pointer to right pointer. Store greater value in new array and increment/decrement pointer
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else: 
                square = nums[left]
                left += 1
            # square value and store in result list 
            result[i] = square * square

        # return result  
        return result 

#Time comp: O(n)
#Space comp: O(N)