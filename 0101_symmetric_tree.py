#2025-6-9 time: 14:32
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def isMirror(left,right):
            if left is None and right is None:
                return True
            
            if left is None or right is None:
                return False
            
            if left.val == right.val:
                return isMirror(left.left,right.right) and isMirror(left.right,right.left)
            return False
        if root is None:
            return True
        left = root.left
        right = root.right
        return isMirror(left,right)