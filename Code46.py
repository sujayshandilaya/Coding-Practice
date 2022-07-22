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
                    
                else:
                    num_dict[-(nums[i]+nums[j])]=nums[j]
        return op
