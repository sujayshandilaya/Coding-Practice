class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #c2=Counter(nums2)
        c2={}
        for num in nums2:   #This method is faster than counter method.
            c2[num]=c2.get(num,0)+1
        res=[]
        
        for num in nums1:
            if num in c2 and c2[num]>0:
                res.append(num)
                c2[num]-=1
        
        return(res)

#############

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1,nums2=sorted(nums1),sorted(nums2)
        p,q,res=0,0,[]
        
        while p<len(nums1) and q<len(nums2):
            if nums1[p]<nums2[q]:
                p+=1
            elif nums1[p]>nums2[q]:
                q+=1
            else:
                res.append(nums1[p])
                p+=1
                q+=1
        
        return res