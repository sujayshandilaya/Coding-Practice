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
        
        if (x<0) : # This condition can be added by an OR operator (x>0 and x%10 == 0)
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
             
################################
class Solution:
    def isPalindrome(self, x: int) -> bool:

	    if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
		    return False
	
	    result = 0
	    while x > result:
		    result = result * 10 + x % 10
		    x = x // 10
		
	    return True if (x == result or x == result // 10) else False
        