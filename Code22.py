class Solution:
    def isHappy(self, n: int) -> bool:
        square=set()
        while n != 1:
                temp = n
                sum=0
                while(temp!=0):
                    sum = sum + pow((temp%10),2) # Long method
                    temp=int(temp/10)
                print(sum)
                n=sum
                if n in square:
                    return False
                else:
                    square.add(n)      
        return True
   
#####easy method to calculate sum of square of digit

import sys
class Solution:
    def isHappy(self, n: int) -> bool:
        square=set()
        while n != 1:
                n= sum([int(i)*int(i) for i in str(n)]) #easy method
                if str(n) in square:
                    return False
                else:
                    square.add(str(n))      
        return True   
        