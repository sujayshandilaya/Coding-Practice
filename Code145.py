#SLiding window Approach
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq_dict= defaultdict(int)
        k=3
        i,j,cnt=0,0,0    
        while j < len(s):
            freq_dict[s[j]]+=1
            if j>=k-1:
                if len(freq_dict)==k:
                    cnt+=1
                freq_dict[s[i]]-=1
                if freq_dict[s[i]]==0:
                    del freq_dict[s[i]] 
                i+=1
            j+=1
        return(cnt)
        
#############

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==3:
                ans+=1
        return ans