class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        set1=set(nums1)
        set2=set(nums2)
        res=[]
        for num in set1:
            if num in set2:
                res.append(num)
        
        return res

################

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict={}
        for nums in nums1:
            num_dict[nums]=1
        
        res=[]
        for ele in nums2:
            if ele in num_dict and num_dict[ele]!=2:
                res.append(ele)
                num_dict[ele]+=1
        
        return(res)
    