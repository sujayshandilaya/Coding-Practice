 class Solution:
# Brute Force O(n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while i<len(nums) and nums[i]<=target:
            i=i+1
        
        if nums[i-1]==target:
            return(i-1)
        else: 
            return(i)
       
# Binary Search O(log n)
#Recursive Approach
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def rec_binary(arr, l,r,target) -> int:
                mid = l+int((r-l)/2)
                if (r >= l):
                    if (arr[mid]==target):
                        return(mid)
                
                    elif (arr[mid]>target):
                    
                        return rec_binary(arr,l,(mid-1),target)
                    else:
                    
                        return rec_binary(arr,mid+1,r,target)
                else:
                    return mid
            
        index = rec_binary(nums,0,len(nums)-1,target)
        print(index)
        return index

#Iterative Approach

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            if target<nums[left]: return left
            if target > nums[right]: return (right+1)
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
                



 #new method O(log(n))
 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
