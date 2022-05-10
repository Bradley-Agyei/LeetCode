class Solution(object):
    def findMinInRotatedSortedArray(self, nums):
        # init length, left, right 
        length = len(nums)
        left, right = 0, length - 1

        # base case 
        if length == 1:
            return nums[0]

        # check to make sure array is still in ascending order or has been rotated
        if nums[left] < nums[right]:
            return nums[left]

        # ensure within bounds
        while (left < right): 
            # find mid
            mid = left + (right - left) // 2

            # determine which side of array to search 
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1

            # find smallest element based off of these two cases
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

#Time comp: O(log n)
#Space comp: O(1)