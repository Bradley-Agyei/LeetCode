# TrieNode class 
class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    # addWord function 
    def addWord(self, word):
        cur = self 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution(object):
    def wordSearch(self, board, words):
        # init root and add words to trie 
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # init row, cols, result, and visited sets
        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        # dfs/backtracking function 
        def dfs(r, c, node, word):
            # conditions that will return nothing 
            if (r < 0 or c < 0 or 
                r == rows or c == cols or 
                board[r][c] not in node.children or 
                (r, c) in visited):
                return 

            # add to visited set 
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                result.add(word)

            # check all 4 directions 
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

        # iterate through entire board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(result)
