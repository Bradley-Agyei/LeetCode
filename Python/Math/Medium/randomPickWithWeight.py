import random

class Solution(object):
    def __init__(self, w):
        # init prefix_sum list, prefix_sum 
        self.prefix_sum = []
        prefix_sum = 0

        # loop through weights in w 
        for weight in w:
            # add weights to pre_fix sum 
            prefix_sum += weight
            # append prefix_sums to our list 
            self.prefix_sum.append(prefix_sum)

        # set total_sum to prefix_sum 
        self.total_sum = prefix_sum 


    def pickIndex(self):
        # generate a random number
        random_number = self.total_sum * random.random() 
        # init low, high pointers
        low, high = 0, len(self.prefix_sum)

        # ensure inbounds 
        while low < high:
            # init mid point and perform binary search 
            mid = low + (high - low) // 2
            if random_number > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low 