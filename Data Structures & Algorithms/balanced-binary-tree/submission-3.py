# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def balance(node):
            if not node: return 0 


            left = balance(node.left)
            right = balance(node.right)


            if abs(left-right) > 1:
                self.bal = False

            return 1+max(left,right)


    

        balance(root)
        return self.bal