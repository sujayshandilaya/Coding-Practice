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
            
            
            
            