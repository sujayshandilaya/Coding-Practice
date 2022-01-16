class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_strip= s.rstrip()
        words=s_strip.split(" ")
        return(len(words[-1]))

##############

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                length+=1
            elif length!=0:
                break
        
        return length
