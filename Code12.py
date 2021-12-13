class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)-1
        i=0
        while i <=length:
            if(nums[i]==val):
                del nums[i]
                length-=1
            else:
                i+=1
        return(len(nums))
                
