class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        #num_list=list(num)
        op=""
        
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                op="".join(num[0:i+1])
                return op
        return op