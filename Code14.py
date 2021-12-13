class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while i<len(nums) and nums[i]<=target:
            i=i+1
        
        if nums[i-1]==target:
            return(i-1)
        else: 
            return(i)
       
https://leetcode.com/problems/search-insert-position/