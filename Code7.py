class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict={
            '(':')',
            '[':']',
            '{':'}'
        }
        
        stack=[]
 
        for i in range(len(s)):
            if(s[i] in parenthesis_dict.keys()):
                stack.append(s[i])
            elif(s[i] in parenthesis_dict.values()):
                if(len(stack)==0):
                    return(False)
                elif(parenthesis_dict[stack.pop()] != s[i]):
                    return(False)

        if len(stack)==0:
            return(True)
        else:
            return(False)

#

class Solution(object):
    def isValid(self, s):
        d = {'N':0,'(':')', '{':'}','[':']'}
        stack = ['N']
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 1 # 3
            
            
            