class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(root):
            if root:  
                if low<=root.val<=high:
                    self.op+=root.val
                if root.val > low:   
                    inorder(root.left)
                if root.val < high:
                    inorder(root.right)
        self.op=0
        inorder(root)
        return self.op

####################################

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(root):
            op=0
            if root:
                op+=(inorder(root.left))  
                if low<=root.val<=high:
                    op+=root.val
                op+=(inorder(root.right))
            return op
        
        op=inorder(root)
        return op