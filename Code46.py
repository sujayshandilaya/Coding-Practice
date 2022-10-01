class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k])==0:
                        triplets.append([nums[i],nums[j],nums[k]])
        
        return(list(set(tuple(sorted(sub)) for sub in triplets)))


#################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        for i in range(len(nums)):
            dict_triplets={}
            for j in range(i+1,len(nums)):
                if nums[j] in dict_triplets.keys():
                    triplets.append([nums[i],nums[j],dict_triplets[nums[j]]])
                else :
                    dict_triplets[-(nums[i]+nums[j])]=nums[j]
  
        return(list(set(tuple(sorted(sub)) for sub in triplets)))

#################################
07/22/2022:
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=j=k=0
        op=set()
        n=len(nums)
        for i in range(n):
            num_dict={}
            for j in range(i+1,n):
                if nums[j] in num_dict:
                    op.add(tuple(sorted([nums[i],nums[j],num_dict[nums[j]]])))
                    
###########

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        op=[]
        for i in range(n-2):
            if nums[i]>0: break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if temp>0:r-=1
                elif temp<0: l+=1
                else: 
                    op.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: l+=1
                    while l<r and nums[r]==nums[r-1]: r-=1
                    l+=1
                    r-=1
        return op

        
                    
                    
                else:
                    num_dict[-(nums[i]+nums[j])]=nums[j]
        return op
