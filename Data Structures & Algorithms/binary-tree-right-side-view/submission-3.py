# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def level(node,lvl):
            if not node: return

            if len(res) == lvl:
               res.append(node.val)
      

            level(node.right,lvl+1)
            level(node.left,lvl+1)



        

        level(root,0)
        return res