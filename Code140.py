class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            nums.insert(0, nums.pop())
#Its similar to brute force method, whcih takes large amoutn of time to run

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n=len(nums)
        k=k%n
        nums[:] = list(nums[n-k:] + nums[:n-k])
#This takes O(n) space due to list slicing, which internally creates a temporary array
###########
class Solution:
    def rotate(self, nums, k) -> None:
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            start += 1
            end -= 1