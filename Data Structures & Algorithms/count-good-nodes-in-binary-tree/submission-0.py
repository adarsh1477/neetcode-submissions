# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c = 0
        def count(node,best):
            if not node: return None


            if node.val >= best:
                self.c += 1



            left = count(node.left,max(best,node.val))
            right = count(node.right,max(best,node.val))

            


        count(root,root.val)
        return self.c