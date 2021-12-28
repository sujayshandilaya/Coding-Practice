class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_water=0
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                
                water=(j-i)*nums[j] if nums[j]<nums[i] else (j-i)*nums[i]
                
                max_water=max(max_water,water)
        
        return(max_water)

##############

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_water=0
        i,j = 0,len(nums)-1
        while i<=j:
            water=(j-i)*nums[j] if nums[j]<nums[i] else (j-i)*nums[i]
            if nums[j]<nums[i] :
                water=(j-i)*nums[j]
                j-=1
            else:
                water=(j-i)*nums[i]
                i+=1
            max_water=max(max_water,water)
        
        return(max_water)
            
                             
            
        
