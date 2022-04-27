#Problem: Given an array of integers and a target value, return the indices of the two nums that equal target
#Input: [2,7,11,15], target = 9, output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        # init hashmap 
        hashmap = {}
        n = len(nums)

        # loop through nums and see if difference of currentNum - target is already in hashmap: if so return indices
        for i in range(n):
            difference = target - nums[i]
            if difference in hashmap:
                return [i, hashmap[difference]]
            hashmap[nums[i]] = i

#Time comp: O(n)
#Space comp: O(n)