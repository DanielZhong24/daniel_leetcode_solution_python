#2025-10-22 time: 8:36
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        x=0
        while a and a.next:
            a = a.next
            x+=1
        b = headB
        y=0
        while b and b.next:
            b = b.next
            y+=1
        if a!=b:
            return None
        x+=1
        y+=1
        
        a = headA
        b = headB
        if x < y:
            for i in range(y-x):
                b=b.next
        elif x > y:
            for i in range(x-y):
                a = a.next

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
        
        