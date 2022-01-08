class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        return(haystack.find(needle))
        

##############
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and haystack[i:i+len(needle)]==needle:
                return i
                
        return(-1)