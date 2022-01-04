class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=sorted(s)
        t_list=sorted(t)
        
        return True if s_list==t_list else False
            #return


##############
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        
 
        for ele in s:
            dict_s[ele]= dict_s.get(ele,0)+1
        for ele in t:
            dict_t[ele]= dict_t.get(ele,0)+1
        return dict_s==dict_t

###############
