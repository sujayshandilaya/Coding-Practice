class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        string=[None]*len(s)
        for i in range(len(s)):
            string[indices[i]]=s[i]
        
        return(''.join(string))
		
#################
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for index, char in enumerate(s):
            res[indices[index]] = char
        return "".join(res)