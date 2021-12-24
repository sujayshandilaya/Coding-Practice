class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=int((left+right)/2)
            
            while left < mid and nums[left] == nums[mid]: # tricky part
                left += 1
            
            if nums[mid]==target : return True
            
            elif nums[left]<=nums[mid]:
                
                if( nums[left] <= target < nums[mid]):
                    right=mid-1
                else:
                    left=mid+1
            else:
                if( nums[mid] < target <= nums[right]):
                    
                    left=mid+1
                else:
                    right=mid-1
        
        return False