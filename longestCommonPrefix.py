class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len=min([len(ele) for ele in strs])
        op=""
        for i in range(min_len):
            str=strs[0][i]
            for s in strs:
                if s[i]!=str:
                    return op
            op+=str
        return op

------------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first=strs[0]
        last=strs[-1]
        ans=""
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans

---------------------------------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix=strs[0]
        for string in strs:
            while not string.startswith(prefix):
                prefix=prefix[:-1]
        
        return prefix
