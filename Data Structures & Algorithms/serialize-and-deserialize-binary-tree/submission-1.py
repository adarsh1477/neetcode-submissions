# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        q,res = deque([root]),[]

        while q:
            curr = q.popleft()
            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

            else:
                res.append("null")

        return ','.join(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])


        i=1
        while q:
            curr = q.popleft()
            if i<len(nodes) and nodes[i]!= "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i+=1
            if i<len(nodes) and nodes[i]!= "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)


            i+=1

        return root

        