class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_prof=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                max_prof=max(max_prof,nums[j]-nums[i])
        
        return max_prof
        
######################

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_prof=0
        n=len(nums)
        initial_min=nums[0]
        for i in range(n):
                initial_min=min(initial_min,nums[i])
                max_prof=max(max_prof,nums[i]-initial_min)
        return max_prof
