from collections import deque

class Solution(object):
    def rightSideView(self, root):
        # init queue, result_list
        queue = deque([root])
        result_list = []

        # while queue is not empty
        while queue:
            queue_length = len(queue)
            right_most_value = None 

            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    right_most_value = node 
                    queue.append(node.left)
                    queue.append(node.right)
            if right_most_value:
                result_list.append(right_most_value.val)

        return result_list 



