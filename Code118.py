class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def checkPattern(word1: str, word2: str):
            new_dict={}
            for i in range(len(word1)):
                if (word1[i] in new_dict and new_dict[word1[i]]!=word2[i]) or (word1[i] not in new_dict and word2[i] in new_dict.values()):
                    return False
                else:
                    new_dict[word1[i]]=word2[i]
            
            return True
        output=[]
        for word in words:
            if checkPattern(pattern,word): output.append(word)
        
        return output
####removed function call

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output=[]
        for word in words:   
            new_dict={}
            for i in range(len(pattern)):
                if (pattern[i] in new_dict and new_dict[pattern[i]]!=word[i]) or (pattern[i] not in new_dict and word[i] in new_dict.values()):
                    break
                else:
                    new_dict[pattern[i]]=word[i]
            else:
                output.append(word)           
        return output
		

###################

