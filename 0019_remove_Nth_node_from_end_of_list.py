#2025-3-16 time: 8:22
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        first,second = head,head

        for i in range(n): 
            first = first.next

        if not first:
            return head.next
        
        while first.next:
            first,second = first.next,second.next

        second.next = second.next.next

        return head
        
