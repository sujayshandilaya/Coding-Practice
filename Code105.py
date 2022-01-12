class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        letters=set(words[0])
        res=[]
        
        for letter in letters:
            n = min([word.count(letter) for word in words])
            
            res+=[letter]*n
        
        return res