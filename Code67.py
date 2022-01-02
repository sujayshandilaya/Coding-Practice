### This problem states that L and R shoule be equal in a substring. we have to count the no of sub string which can have equal no of L and R.

'''
Hence we maintain a counter, which increases if it finds a L and decreases if it finds a R.
whenever the counter = 0, it means the string is balanced.
'''
###
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt=res=0
        
        for letter in s:
            cnt+=1 if letter=="L" else -1
            #print(cnt)
            if cnt==0:
                res+=1
        
        return(res)


#########
'''
In this solution, we have maintained 2 counters, one for L and one for R. after each character compare the two counters. If the counters are equal, then its counted as a substirng. 
'''


class Solution(object):
    def balancedStringSplit(self, s):
        w_count = l_count = r_count = 0
        for ch in s:
            if ch == "L":
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                w_count += 1
        return w_count
        
