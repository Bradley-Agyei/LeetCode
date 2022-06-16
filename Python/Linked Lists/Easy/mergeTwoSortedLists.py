class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class Solution(object):
    def mergeLists(self, list1, list2):
        # init prehead variable 
        prehead = ListNode()

        # set previous to prehead 
        previous = prehead

        # run while both lists are full
        while list1 and list2:
            # compare values from list 
            if list1.val < list2.val:
                previous.next = list1
                list1 = list1.next
            else:
                previous.next = list2
                list2 = list2.next

            previous = previous.next

        # check to make sure if there are remaining values in either list 
        if list1:
            previous.next = list1
        elif list2:
            previous.next = list2 
        
        return prehead.next

# Time Comp: O(m + n)
# Space comp: O(1)