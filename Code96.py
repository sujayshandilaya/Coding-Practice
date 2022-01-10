class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        for i in range(97,123):
            if chr(i) not in sentence:
                return False
        return True

############

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        word=set(sentence)
        
        return True if len(word)==26 else False

##############
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        word=[-1]*26
        
        for i in sentence:
            word[ord(i)-97]=0 
        if -1 in word:
            return False
        else:
            return True