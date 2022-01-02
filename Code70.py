class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        queue=[]
        count=0
        
        for paranthesis in s:
            if paranthesis=='(':
                queue.append(paranthesis)
            elif paranthesis==")" and len(queue)>0:
                queue.pop()
            else:
                count+=1
        return(count+len(queue))


###################
###This is an unoptimized solution to this problem.
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        while "()" in S:
            S = S.replace("()", "")
        
        return len(S)

