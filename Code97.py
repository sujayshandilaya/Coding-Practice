class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        start=0
        stack=[]
        new=''
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')' and len(stack)==1:
                stack.pop()
                new+=s[start+1:i]
                start=i+1
            else:
                stack.pop()
        
        return new
##################        
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []
        
        bucket=''
        
        for s in S:
            
            if s =='(':
                stack.append(s)
            else:
                stack.pop()
            bucket+=s
            if len(stack)==0:
                res+=(bucket[1:-1])
                bucket=''
            
        return res