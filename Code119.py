class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keys=['qwertyuiop','asdfghjkl','zxcvbnm']
        output=[]
        for word in words:
            for key in keys:
                if word[0].lower() in key:
                    row=key
            for letter in word:
                if letter.lower() not in row:
                    break
            else:
                output.append(word)
        return output
        
                    