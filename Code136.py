class Solution:
    def minOperations(self, s: str) -> int:
        
        ptr1='1'
        ptr0='0'

        cnt0=0 if s[0]==ptr0 else 1
        cnt1=0 if s[0]==ptr1 else 1
        
        for i in range (1,len(s)):
            if ptr0==s[i]:
                print(i,ptr0)
                cnt0+=1
            if ptr1==s[i]:
                cnt1+=1
    
            ptr0='0' if ptr0=='1' else '1'
            ptr1='0' if ptr1=='1' else '1'

        return min(cnt0,cnt1)

##########

   def minOperations(self, s):
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)
        
##################

class Solution:
    def minOperations(self, s: str) -> int:
        cnt=cnt1=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='0':
                    cnt1+=1
                else:
                    cnt+=1
            else:
                if s[i]=='0':
                    cnt+=1
                else:
                    cnt1+=1
        return min(cnt,cnt1)
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        