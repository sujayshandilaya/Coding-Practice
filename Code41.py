class Solution:
    running=[None]
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        running=[None]*len(nums)
        for i in range(len(nums)):
            running[i]=sums=sums+nums[i]

        return(running)
