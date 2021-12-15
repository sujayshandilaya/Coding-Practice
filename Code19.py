# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1=[]
        def traverse_inorder(root:Optional[TreeNode]):
            
            if root:
                traverse_inorder(root.left)
                
                l1.append(root.val)
                print(root.val)
                
                traverse_inorder(root.right)
            return(l1)
        
        
        return(traverse_inorder(root))
                
        

            
        