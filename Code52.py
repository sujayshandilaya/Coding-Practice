class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''.join(c.lower() for c in s if c.isalnum())
        i=0
        j=len(string)-1
        while i<=j:
            if string[i]!=string[j]:
                return False
            else:
                i+=1
                j-=1
        return(True)
        
###########

class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]