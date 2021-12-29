class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=2
        while i<n:
            print(i)
            if nums[i]==nums[i-1]==nums[i-2]:
                del nums[i]
                n-=1
            else:
                i+=1
        
        return(len(nums))

#############

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+2
        while j<n:
            if nums[i]==nums[j]:
                del[nums[j]]
                n-=1
            else:
                i+=1
                j=i+2
        
        return(len(nums))