

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return True if "".join(word1)=="".join(word2) else False

############
class Solution:
    
    def generate(self,words:List[str]):
        
        for word in words:
            for letter in word:
                yield letter
        
        yield None
    
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1!=c2:
                return False
        
        return True

#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/1007878/Python-Understanding-generators-and-yield-statement