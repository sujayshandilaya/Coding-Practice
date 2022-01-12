class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        top=0
        for i in range(len(arr)):
            if arr[i]>top:
                top=arr[i]
                index=i
        
        return index

##########

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=1
        right=len(arr)-1
        while(left<=right):
            mid=int((left+right)/2)
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid-1]<arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid-1

'''
Its given that all left elements will be in ascenidng than peak and right elements will also be descending than peak
Eliminated first because anyways the peak would never be those elements
There exists some i with 0 < i < arr.length - 1 such that..., it means the answer is in range [1..n-1]
'''
