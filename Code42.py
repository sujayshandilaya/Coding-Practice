class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans=[None]*len(nums)
        
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        
        return(ans)
        
        

######
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        #ans=[None]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            nums[i]=nums[i] + n*(nums[nums[i]]%n)
        
        for i in range(n):
            nums[i]=int(nums[i]/n)
        
        return(nums)

#https://leetcode.com/problems/build-array-from-permutation/discuss/1452892/O(n)-time-and-O(1)-space-solution-with-explanation.