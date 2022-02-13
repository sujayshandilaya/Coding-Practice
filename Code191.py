class Solution:
    def convert(self, string: str, k: int) -> str:
        if k == 1 or k >= len(string):
            return string
        op=[""]*k
        step=1
        index=0
        
        for s in string:
            op[index]+=s
            
            if index==0:
                step=1
            elif index==(k-1):
                step=-1
            
            index+=step
        
        return("".join(op))
            
            
        