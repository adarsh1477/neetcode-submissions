# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def good(node,best):
            if not node: return

            if node.val >= best:
                self.count += 1

            good(node.left,max(best,node.val))
            good(node.right,max(best,node.val))
        


        good(root,root.val)
        return self.count