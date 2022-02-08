class Solution:
    running=[None]
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        running=[None]*len(nums)
        for i in range(len(nums)):
            running[i]=sums=sums+nums[i]

        return(running)

###################

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        
        running=[nums[0]]
        
        for i in range(1,len(nums)):
            running.append(running[-1]+nums[i])

        return(running)

####################

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        running=[None]*len(nums)
        running[0]=nums[0]
        
        for i in range(1,len(nums)):
            running[i]=(running[i-1]+nums[i])

        return(running)

