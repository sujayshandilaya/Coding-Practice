class Solution:
    def arrangeWords(self, text: str) -> str:
        n=" ".join(sorted(text.split(), key=len))       
        return(n.capitalize()) 

class Solution:
    def arrangeWords(self, text: str) -> str:
        return((" ".join(sorted(text.split(), key=len))).capitalize())
        
class Solution:
    def arrangeWords(self, text: str) -> str:
        len_dict=defaultdict(list)
        string=[]
        
        for word in text.split():
            len_dict[len(word)].append(word)
        
        for length in sorted(len_dict.keys()):
            string+=len_dict[length]
         
        return(" ".join(string).capitalize())