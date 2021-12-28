class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                newTarget=(target-nums[i]-nums[j])
                k,l=j+1,len(nums)-1
                while k<l:
                    if nums[k]+nums[l] == newTarget:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif nums[k]+nums[l] < newTarget:
                        k+=1
                    else:
                        l-=1
        
        return(res)
                
                
                    
                
################
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<=3:  return [] 
        res=set()
        seen=set()
        temp=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    newTarget=target-nums[i]-nums[j]-nums[k]
                    
                    if newTarget in seen:
                        temp=sorted([nums[i],nums[j],nums[k],newTarget])
                        res.add((temp[0],temp[1],temp[2],temp[3]))
            seen.add(nums[i])
                    
        return(res)
                
                
                    
                
                
        