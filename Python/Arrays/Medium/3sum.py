class Solution(object):
    def threeSum(self, nums):
        # init length, result
        length = len(nums)
        result = []
        
        # sort nums
        nums.sort()

        # iterate through nums 
        for i in range(length):
            # condition: if current num > 0, break 
            if nums[i] > 0:
                break

            # condition: check to see if current num == 0 or current num == prev num then call twoSumII
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, result)

        # return result
        return result 


    #twoSumII function that will be used to solve problem
    def twoSumII(self, nums, i, result):
        # init pointers, length of nums
        length = len(nums)
        left, right = i + 1, length - 1

        # condition: while left < right
        while (left < right):

            # init sum 
            sum = nums[i] + nums[left] + nums[right]

            # check to see if sum > or < 0, increment/decrement pointers accordingly 
            if sum < 0:
                left += 1
            elif (sum > 0):
                right -= 1
            else:
                # condition: triplets found, store in results array and increment/decrement pointers 
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # condition: ensure num is not a duplicate
                while left < right and nums[i] == nums[i - 1]:
                    left += 1
        # return result 
        return result 

#Time comp: O(n^2)
#Space comp: O(n)
