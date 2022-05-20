class Solution(object):
    def exist(self, board, word):
        # init rows, col, path set for visited cells
        rows, cols = len(board), len(board[0])
        path = set()

        # dfs (backtracking) function 
        def dfs(r, c, i):
            # base case 
            if i == len(word):
                return True

            # conditions that will return false
            if (r < 0 or cols < 0 or 
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r,c) in path):
                return False 

            # add r,c to path 
            path.add((r,c))

            # check all 4 directions 
            result = (dfs(r + 1, c, i + 1) or 
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1))

            # remove r,c from path 
            path.remove((r,c))

            # return result 
            return result 

        # iterate through the entire board and return true if dfs is true 
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True 
        # return false if word is not found 
        return False 