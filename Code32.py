class Solution:
    def mySqrt(self, x: int) -> int:
        
        low=0
        high=int(x/2)
        
        while low <= high : 
            mid=int((low+high)/2)
            if x >= pow(mid,2) and x < pow((mid+1),2) :  #if pow(mid,2)<= x < pow((mid+1),2) :Either will work
                return(mid)
            elif pow(mid,2)>x:
                high=mid-1
            else:
                low=mid+1 
        
        return(1)
