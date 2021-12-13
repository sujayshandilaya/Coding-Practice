class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)-1
        i=0
        while i < length:
            if(nums[i]==nums[i+1]):
                del nums[i]
                length-=1
            else:
                i+=1
        return(len(nums))
 