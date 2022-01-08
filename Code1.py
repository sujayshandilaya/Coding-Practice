class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        n=len(nums)
        ans = [None] * 2*n
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return (ans)
        
#####################
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
           
        return nums*2
            
