# TrieNode class
class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# Word Dict class
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    # function used to insert a word into dictionary 
    def addWord(self, word):
        # set cur -> root
        cur = self.root 

        # iterate word char by char and add to dict if not present 
        for c in word:
            if c not in cur.children():
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True 

    def search(self, word):
        
        # dfs function 
        def dfs(j, root):
            cur = root
 
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False 
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)

# Correct algorithm but time limit exceeded in LC because of changed test cases 
    