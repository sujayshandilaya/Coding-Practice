class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        
        op=[None]*n
        op[0]=1
        op[1]=2
        op[2]=2
        for i in range(2,n):
            op[i]= op[i-1]+op[i-2]
        
        return op[-1]