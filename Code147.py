import sys

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        add,i,j=0,0,0
        max_add=-sys.maxsize - 1
        
        for j in range(len(nums)):
            add+=nums[j]
            if j >= k-1:
                max_add=max(max_add, add)
                add-=nums[i]
                i+=1
        
        return(max_add/k)

#1. for comapring the avgs, we can find the maximum value. The value which is max, will have max avg as well.
############

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0        
        max_add=add=sum(nums[:k])
        for i in range(k,len(nums)):
            
            add+=(nums[i]-nums[i-k])
            max_add=max(max_add, add)

        return(max_add/k)

#insetad of adding next element and removing first element, we can do both of these is one step only
        