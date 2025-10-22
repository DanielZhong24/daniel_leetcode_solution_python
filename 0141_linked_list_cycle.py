#2025-10-21 time: 9:20
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        prev = head
        curr = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next

            if prev == curr:
                return True

        return False
