class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        cnt=0
        while i<n:
            if nums[i]==0:
                del nums[i]
                cnt+=1
                n-=1
            else:
                i+=1
        for i in range(cnt):
            nums.append(0)
            
##############

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        x=len(nums)
        i=0
        cnt=0
        while i<n:
            if nums[i]==0:
                n-=1
                nums.insert(x-1, nums.pop(i))
            else:
                i+=1https://leetcode.com/problems/move-zeroes/