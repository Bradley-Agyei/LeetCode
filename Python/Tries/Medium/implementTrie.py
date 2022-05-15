# TrieNode class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 

# Trie class 
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    #insert function 
    def insert(self, word):
        #set cur to root
        cur = self.root 

        # go char by char in word and add to Trie if not already present 
        for c in word:
            if c not in cur.children:               # if char is not in children 
                cur.children[c] = TrieNode()        # add char 
            cur = cur.children[c]
        cur.endOfWord = True                        # set endOfWord to True

    #search function
    def search(self, word):
        # set cur to root
        cur = self.root

        # iterate char by char and search children
        for c in word:          
            if c not in cur.children:               #if char is not in children - return False
                return False
            cur = cur.children[c]
        return cur.endOfWord                        # return True if endOfWord returns true 

    #startsWith function
    def startsWith(self, prefix):
        # set cur to root
        cur = self.root

        # iterate char by char in prefix to see if its in children
        for c in prefix:
            if c not in cur.children:               # if char is not in children - return false 
                return False
            cur = cur.children[c]
        return True 
