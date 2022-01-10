class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:

            if word==word[::-1]:
                    return word
        return ""

################

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:

            left=0
            right=len(word)-1
            while left<right:
                if word[left]!=word[right]:
                    break
                else:
                    left+=1
                    right-=1
            else:
                return word
        return ""
                    
        