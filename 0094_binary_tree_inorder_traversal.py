#2025-10-22 time: 2:37
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)
        traverse(root)
        return result
