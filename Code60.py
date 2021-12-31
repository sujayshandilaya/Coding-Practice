class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len=0
        for sentence in sentences:
            max_len=max(max_len,len(sentence.split()))
        
        return(max_len)
		
		
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
		return(max(len(s.split()) for s in sentences))
		


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(" ") for s in sentences) + 1
		

s.count() is faster method because it doesnt create an array internally. 