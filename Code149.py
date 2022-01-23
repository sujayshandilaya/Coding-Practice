class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic={}
        cnt=l=r=a=b=c=0
        n=len(s)
        while r < n:
            if s[r]=='a': a+=1
            elif s[r]=='b' : b+=1
            else: c+=1   
            while a>0 and b>0 and c>0:
                cnt+= (n-r)
                if s[l]=='a': a-=1
                elif s[l]=='b' : b-=1
                else: c-=1
                l+=1
            r+=1
        
        return cnt