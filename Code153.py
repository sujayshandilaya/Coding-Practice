class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        cnt= 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if cnt or ( i > 1 and i < len(nums)-1 and nums[i]<nums[i-2] and nums[i+1] < nums[i-1]):
                    return False
                cnt=1
        return True