class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntr=Counter(s)
        cnt=0
        for letter in t:
            if letter in cntr and cntr[letter]>0:
                cntr[letter]-=1
            else:
                cnt+=1
        return cnt