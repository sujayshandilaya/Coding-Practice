# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p != None and q!=None:
                if p.val!=q.val:
                    return(False)
                else:
                    return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
            elif p == None and q==None:
                return(True)
            else:
                return(False)
                    
                
                
                
  #Method2              
                
		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:		
		        
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return p is q  #It is just to return True if p==None and q==None else False