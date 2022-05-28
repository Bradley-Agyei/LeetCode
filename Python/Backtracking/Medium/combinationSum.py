class Solution(object):
    def combinationSum(self, candidates, target):
        # results list 
        results = []

        # backtrack function 
        def backtrack(left_over, combination, start):
            # base case: target is reached
            if left_over == 0:
                results.append(list(combination))
                return

            # base case: target is not reached 
            elif left_over < 0:
                return

            # iterate through entire list for possible combinations 
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(left_over - candidates[i], combination, i)
                combination.pop()
                
            # call backtrack function 
            backtrack(target, [], 0)

            # return results 
            return results 