class Solution:
    def reverse(self, x: int) -> int:
        
        def revInt(x):
            num=0
            while x:
                num=(num*10+ (x%10))
                x=(x//10)
            return 0 if num > pow(2, 31) else num
        
        if x > 0:
            return revInt(x)
        else:
            return -revInt(-x)