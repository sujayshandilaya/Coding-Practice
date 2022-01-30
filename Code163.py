class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new_nums,odd,even=[None]*len(nums),1,0
        for num in nums:
            if num>=0:
                new_nums[even]=num
                even+=2
            else:
                new_nums[odd]=num
                odd+=2
        return new_nums

###################

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums,negative_nums=[],[]
        i,j=0,0
        for num in nums:
            if num>=0: positive_nums.append(num)
            else: negative_nums.append(num)
        while j < len(nums):
            nums[j], nums[j+1]=positive_nums[i], negative_nums[i]
            i+=1
            j+=2
        return nums