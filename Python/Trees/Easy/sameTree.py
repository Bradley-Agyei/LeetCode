class Solution(object):
    def sameTree(self, p, q):
        # check each case 
        # 1. if p AND q are empty, return true 
        if not p and not q:
            return True

        # 2. if p OR q are empty, return false 
        if not p or not q:
            return False

        # 3. compare val or p and q
        if p.val != q.val:
            return False 

        # recursively call on p and q children 
        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))

#Time comp: O(n)
#Space comp: 