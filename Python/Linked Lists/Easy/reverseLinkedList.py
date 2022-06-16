class Solution(object):
    def reverseList(self, head):
        # init current, previous 
        current = head
        previous = None 

        while current:
            temp = current
            current.next = previous
            previous = current
            current = temp 

        return previous 

# iterative approach 
# time comp: O(N)
# Space comp: O(1)