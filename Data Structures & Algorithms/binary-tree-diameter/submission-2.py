# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = float("-inf")

        def diametre(node):
            if not node:
                return 0

            left = diametre(node.left)
            right = diametre(node.right)

            self.d = max(self.d,left+right)

            return 1+max(left,right)
            

        
        diametre(root)
        return self.d