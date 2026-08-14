
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i,val in enumerate(inorder): idx[val] = i


        def Construct(ps,pe,ist,ie):
            if ps>pe: return None


            root_val = preorder[ps]
            mid = idx[root_val]
            root = TreeNode(root_val)

            left_size = mid-ist


            root.left = Construct(ps+1,ps+left_size,ist,mid-1)
            root.right = Construct(ps+left_size+1,pe,mid+1,ie)


            return root



        return Construct(0,len(preorder)-1,0,len(inorder)-1)