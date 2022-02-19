class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s:str,l:int,r:int):
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        res=""
        for i in range(len(s)):
            temp=helper(s,i,i+1)
            if len(temp)>len(res):
                res=temp
            temp=helper(s,i,i)
            if len(temp)>len(res):
                res=temp
        return res