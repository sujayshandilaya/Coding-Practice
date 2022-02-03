class Solution:
    def minSwaps(self, s: str) -> int:
        swap,cnt_c,cnt_o=0,0,0
        for bracket in s:
            if bracket=='[':
                cnt_o+=1
            else:
                cnt_c+=1
            if cnt_c>cnt_o:
                swap+=1
                cnt_c-=1
                cnt_o+=1
        return swap