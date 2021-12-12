#Converting to String
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #print(str(x))
        
        y=str(x)
        
        z=y[::-1]
        
        if(z==y):
            return(True)
        else:
        
            return(False)

#without converting

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if (x<0) :
           return(False)
        elif (x==0):
            return(True)
        else:
            num=0
            temp=x
            while(temp!=0):
                rem = temp%10
                temp=int(temp/10)
                num=(num*10)+rem
            if (num==x):
                return (True)
            else:
                return (False)
        