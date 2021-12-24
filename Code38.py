class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left=0
        right=len(nums)-1
        small=nums[left]
        while left<=right:
            
            mid=int((left+right)/2)
            small=min(small,nums[mid])
            
            if(nums[left]<=nums[mid]):
                if small <= nums[left]:
                    left=mid+1
                else:
                    small = nums[left]
                    left=mid+1
            
            else:
                if mid == len(nums)-1:
                    small=min(small,nums[mid])
                    right=mid-1
                elif small <= nums[mid+1]:
                    right=mid-1
                else : 
                    small=nums[mid+1]
                    right=mid-1
        
        return(small)
                    
                    
                    
                    
                    
                    
                    
                    
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid    
        return nums[left]