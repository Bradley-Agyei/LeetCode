class Solution(object):
    def searchInRotatedSortedArray(self, nums, target):
        # init length and pointers 
        length = len(nums)
        left, right = 0, length - 1

        #ensure in bounds 
        while left < right:
            # find mid point
            mid = left + (right - left) // 2

            # return mid whenever mid == target 
            if nums[mid] == target:
                return mid 
            elif (nums[mid] >= nums[left]):
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 

#Time comp: O(log n)
#Space comp: O(1)
