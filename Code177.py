class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        dict_sum={}
        cnt=0
        for i in range(n):
            for j in range(n):
                temp=nums1[i]+nums2[j]
                dict_sum[temp]=dict_sum.get(temp,0)+1    
        for k in range(n):
            for l in range(n):
                temp=(nums3[k]+nums4[l])*(-1)
                cnt+= dict_sum.get(temp,0)
        return cnt
###############################

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        dict_sum={}
        cnt=0
        for i in nums1:
            for j in nums2:
                temp=i+j
                dict_sum[temp]=dict_sum.get(temp,0)+1    
        for k in nums3:
            for l in nums4:
                temp=(k+l)*(-1)
                cnt+= dict_sum.get(temp,0)
        return cnt

#################

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        return sum(counts[-(c + d)] for counts in [Counter(a + b for a in nums1 for b in nums2)] for c in nums3 for d in nums4)