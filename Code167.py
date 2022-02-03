class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:        
        return sorted([num*num for num in nums])
#Accepted Approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:        
        left,right=0,len(nums)-1
        output=[]
        while left <=right:
            
            if abs(nums[left])<=abs(nums[right]):
                output.insert(0,(nums[right]*nums[right]))
                right-=1
            else:
                output.insert(0,(nums[left]*nums[left]))
                left+=1
        return output