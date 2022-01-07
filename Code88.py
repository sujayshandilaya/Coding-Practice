class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters={}
        for letter in s:
            letters[letter]=letters.get(letter,0)+1
        
        for i in range(len(s)):
            if letters[s[i]]==1:
                return i
        
        return -1

#############

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for k,v in Counter(s).items():
            if v==1:
                return s.index(k)
        
        return -1