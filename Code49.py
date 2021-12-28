class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3: return sum(i for i in nums)
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            j,k=i+1, len(nums)-1  
            while j<k:
                sum_num=nums[i]+nums[j]+nums[k]
                if (sum_num==target):
                    return sum_num
                
                if abs(sum_num-target) < abs(result-target):
                    result=sum_num
                
                if sum_num<target:
                    j+=1
                else:
                    k-=1
        
        return(result)
        
        