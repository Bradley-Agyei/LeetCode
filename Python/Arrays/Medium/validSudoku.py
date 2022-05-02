import collections 

class Solution(object):
    def validSudoku(self, board):
        # init hashsets for rows, cols, and subboxes 
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        # loop through rows and cols or board and check whether value already exists in one of the sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sub_boxes[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_boxes[((r//3, c//3))].add(board[r][c])
        return True

#Time comp: O(N^2)
#Space comp: O(N^2)

