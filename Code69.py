class Solution:
    def sortSentence(self, s: str) -> str:
        
        words=s.split(" ")
        shuffled=[None]*len(words)
        for word in words:
            shuffled[int(word[-1])-1] = word[:-1]
            
        return(" ".join(shuffled))
            
        