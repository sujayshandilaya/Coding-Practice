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
    
    ###############################
    
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i,j=0,0
        n=len(nums)
    
        while j < n:
            while j < n and nums[i]==nums[j]:
                j+=1
            if j<n:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return (i+1)
