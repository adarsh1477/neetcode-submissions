# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.answer = -1
        self.count = 0
        def inorder(node,k):
            if not node:
                return

            if self.answer!=-1: return

            inorder(node.left,k)

            self.count += 1

            if self.count == k:
                self.answer = node.val

            inorder(node.right,k)







        inorder(root,k)
        return self.answer