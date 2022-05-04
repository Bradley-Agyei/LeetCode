class Solution(object):
    def longestConsSeq(self, nums):
        # init longest_streak, length of nums, set of nums
        longest_streak = 0
        length = len(nums)
        nums_set = set(nums)

        # base case if nums is empty 
        if not nums:
            return 0 

        # loop through nums_set 
        for num in nums_set:
            # condition if number not in set
            if num - 1 not in nums_set: 
                current_num = num
                current_streak = 1

                # condition if number is in set 
                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1
                # update longest_streak 
                longest_streak = max(longest_streak, current_streak)
        
        # return longest_streak 
        return longest_streak 

#Time comp: O(n)
#Space comp: O(n)