class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m= len(nums1)
        n= len(nums2)
        new_len=m+n
        list1=[None]*(new_len)
        
        j=0
        k=0
        i=0
        
        for i in range(new_len):
            if j==m:
                list1[i]=nums2[k]
                k+=1
            elif k==n:
                list1[i]=nums1[j]
                j+=1
            elif nums1[j]<nums2[k]:
                list1[i]= nums1[j]
                j+=1  
            else:
                list1[i]=nums2[k]
                k+=1
        
        return (list1[int(new_len/2)] + list1[int(new_len/2) -1])/2 if new_len%2==0 else list1[int(new_len/2)]
        
#This is O(m+n) time complexity.

# How to convert it to O(log(m+n)) time complexity?
#Ans - USing binary search
                
                
                
                
                
            
        