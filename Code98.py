# Fails with TLE
class Solution:
    def generateTheString(self, n: int) -> str:
        
        i=1
        output=""
        letters={}
        while i<=n:
            letter=chr(random.randint(97,122))
            letters[letter]=letters.get(letter,0)+1
            if (letters.get(letter))%2!=0:
                output+=letter
                i+=1
            else:
                letters[letter]-=1
        
        return(output)

############
#Correct Solution
class Solution:
    def generateTheString(self, n: int) -> str:
        
        if n%2==0:
            output='x'*(n-1)+'y'
        else:
            output='x'*n
        return(output)