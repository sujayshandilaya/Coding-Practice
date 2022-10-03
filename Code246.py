class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums=sorted(nums)
        op=[sorted_nums.index(n) for n in nums]
        
        return op