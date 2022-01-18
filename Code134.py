class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        s_dict={}
        max_len=-1
        for i in range(len(s)):
            if s[i] in s_dict:
                max_len = max(max_len,(i-s_dict[s[i]]-1))
            else:
                s_dict[s[i]]=i
        
        return(max_len)