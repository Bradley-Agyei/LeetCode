class Solution(object):
    def combinationSum3(self, n, k):            # n = target, k = size of combination list 
        # init results list 
        results = []

        # backtrack function 
        def backtrack(left_over, combination, next_start):
            # condition to append combination list to results list 
            if left_over == 0 and len(combination) == k:
                results.append(list(combination))
                return 

            # condition to stop exploration of possible combinations 
            elif left_over < 0 or len(combination) == k:
                return 

            # iterate through reduced list 
            for i in range(next_start, 9):
                combination.append(i + 1)
                backtrack(left_over - i - 1, combination, i + 1)
                combination.pop()

            # call backtrack function
            backtrack(n, [], 0)

            # return results 
            return results 