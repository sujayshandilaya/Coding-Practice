class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(left, right, flag):
            while left <= right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    if flag:
                        return isPalindrome(left+1, right, False) or isPalindrome(left,right-1, False)
                    else:
                        return False
            return True
        
        return isPalindrome(0, len(s)-1, True)
            
        