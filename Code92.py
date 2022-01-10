class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left=operation=0
        right=len(nums)-1
        
        while left<right:
            
            if (nums[left]+nums[right])==k:
                left+=1
                right-=1
                operation+=1
            elif(nums[left]+nums[right])<k:
                left+=1
            else:
                right-=1
        
        return(operation)
            
##############

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       
        cnt=Counter(nums)
        operation=0
        for num in nums:
            if k-num==num and cnt[k-num]==1:
                cnt[k-num]-=1
            if k-num in cnt.keys() and cnt[k-num]>0 and cnt[num]>0:
                cnt[k-num]-=1
                cnt[num]-=1
                operation+=1
        return(operation)

#################

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       
        cnt={}
        operation=0
        
        for num in nums:
            if k-num in cnt and cnt[k-num]>0:
                operation+=1
                cnt[k-num]-=1
            else:
                cnt[num]=cnt.get(num,0)+1
        
        return(operation)