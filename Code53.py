class Solution:
    def reverseWords(self, s: str) -> str:
        
        words= s.split()
        words=words[::-1]
        
        string=' '.join(word.strip() for word in words)
        
        return(string)