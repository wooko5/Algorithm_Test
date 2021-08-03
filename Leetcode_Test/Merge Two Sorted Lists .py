# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            result = l1
            l1.next = Solution.mergeTwoLists(self,l1.next, l2)
        else:
            result = l2
            l2.next = Solution.mergeTwoLists(self,l2.next, l1)
        return result