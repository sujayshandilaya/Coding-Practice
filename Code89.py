class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict={}
        t_dict={}
        
        for i in range(len(s)):
            s_dict[s[i]]=s_dict.get(s[i],0)+1
            t_dict[t[i]]=t_dict.get(t[i],0)+1
        
        t_dict[t[-1]]=t_dict.get(t[-1],0)+1
        for key, value in t_dict.items():
            if s_dict.get(key,0)!=value:
                return key

###################

def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i