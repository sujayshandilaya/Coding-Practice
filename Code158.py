class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=0
        cntr=Counter(s)
        for i,j in cntr.items():
            if j%2==0:
                cnt+=j
                cntr[i]-=j
            elif j > 1:    
                cnt+=(j-1)
                cntr[i]-=(j-1)
        if 1 in cntr.values():
            cnt+=1
        
        return cnt

#############

class Solution:
    def longestPalindrome(self, string: str) -> int:
        cnt=0
        cntr={}
        for s in string:
            cntr[s]= cntr.get(s,0)+1
            if cntr[s]==2:
                cnt+=2
                del cntr[s]

        if len(cntr):
            cnt+=1
        
        return cnt
