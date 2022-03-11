# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.li=[]
        def LonelyNodes(root):
            if root:
                if root.left and root.right:
                    LonelyNodes(root.left)
                    LonelyNodes(root.right)
                elif root.right:
                    self.li.append(root.right.val)
                    LonelyNodes(root.right)
                    elif root.left:
                        self.li.append(root.left.val)
                        LonelyNodes(root.left)
        
        LonelyNodes(root)
        return self.li