from collections import deque
class Solution(object):
    def levelOrder(self, root):
        #init levels list(results list), level, queue 
        levels = []
        level = 0
        queue = deque([root,])

        # base case
        if not root:
            return levels 

        # condition: while queue is not empty 
        while queue:
            # create empty list in levels 
            levels.append([])

            # determine number of current elements in queue that need to be added to list by finding length of queue 
            level_length = len(queue)

            # iterate through queue and append to list 
            for i in range(level_length):
                # pop nodes 
                node = queue.popleft()
                #append to current level list in levels
                levels[level].append(node.val)

                # add child nodes of the current level in the queue for the next level 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # increment levels
            levels += 1 
        return levels 

# Time comp: O(n)
# Space comp: O(n)
