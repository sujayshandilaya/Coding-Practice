class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()

##########

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m,n=m-1,n-1
        i=len(nums1)-1
        
        for i in range(len(nums1)-1,-1,-1):
            if m==-1:
                nums1[0:i+1]=nums2[0:n+1]
                break
            if n==-1:
                break
            if nums1[m]<=nums2[n]:
                print("inside if")
                nums1[i]=nums2[n]
                n-=1
            else:
                nums1[i]=nums1[m]
                m-=1
