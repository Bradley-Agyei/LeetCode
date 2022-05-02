import collections, heapq
from collections import Counter

class Solution(object):
    def topKFrequentElements(self, nums, k):
        # if k == len(nums) - return nums
        if k == len(nums):
            return nums

        # dict subclass Counter to count integers in nums 
        count = Counter(nums)

        # build heap of k largest elements and convert to an array 
        return heapq.nlargest(k, count.keys(), key=count.get)

#Time comp: O(N log K)
#Space comp: O(N + k)
