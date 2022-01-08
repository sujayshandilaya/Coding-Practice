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
 
 ###########
 class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        n=len(arr)-1
        x=1
        for i in range(n):
            if arr[i]!=arr[i+1]:
                arr[x]=arr[i+1]
                x+=1
        
        return x