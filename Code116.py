class Solution:
    def sortString(self, s: str) -> str:
        n=len(s)
        cntr=Counter(s)
        letter=""
        while n>0:
            for i in range(ord('a'),ord('z')+1):
                char=chr(i)
                if char in cntr and cntr[char]>0:
                    letter+=char
                    cntr[char]-=1
                    n-=1
            if n==0: break
            
            for i in range(ord('z'),ord('a')-1,-1):
                char=chr(i)
                if char in cntr and cntr[char]>0:
                    letter+=char
                    cntr[char]-=1
                    n-=1
            if n==0: break
        return letter
            
#######################

class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        letter=''
        while s:
            for char in sorted(set(s)):
                s.remove(char)
                letter+=char
        
            for char in sorted(set(s), reverse=True):
                s.remove(char)
                letter+=char
        
        return letter