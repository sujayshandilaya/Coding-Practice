class Solution(object):
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return((nums[0]-1)*(nums[1]-1))

###################

class Solution(object):
    def maxProduct(self, nums):
        first,second=0,0
        for n in nums:
            if n >first:
                first,second=n,first
            else:
                second=max(second,n)
        
        return((first-1)*(second-1))

