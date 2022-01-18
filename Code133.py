class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        max_0,max_1,cnt_0,cnt_1=0,0,0,0
        for i in s:
            if i=='1':
                cnt_1+=1
                cnt_0=0
                max_1=max(cnt_1,max_1)
            else:
                cnt_0+=1
                cnt_1=0
                max_0=max(cnt_0,max_0)
        
        print(max_1,max_0)
        return True if max_1>max_0 else False
                
                
        