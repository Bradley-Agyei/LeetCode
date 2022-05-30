class Solution(object):
    def surroundedRegions(self, board):
        # init rows, cols 
        rows, cols = len(board), len(board[0])

        # dfs function help us identify our border cells and its neighbors
        def borderCells(r, c):
            # base case 
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                board[r][c] != 'O'):
                return 

            # change 'O' --> 'T' 
            board[r][c] = 'T'

            # recursively check all for directions 
            for board_row, board_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                borderCells(r + board_row, c + board_col)

        # 1. Use dfs function to change border cells from 'O' --> 'T' 
        # iterate through rows and cols and change cells
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and 
                    r in [0, rows - 1] or 
                    c in [0, cols - 1]):
                    board[r][c] = 'T' 

        # 2. Change remaining 'O' --> 'X'
        # iterate through board and change cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Change 'T' --> 'O' 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

# Time and Space = O(M * N)