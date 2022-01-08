#Brute Force
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left=0
        n=len(arr)-1
        if n==0 or arr[0]>arr[1]:
            return 0
        if arr[n]>arr[n-1]:
            return n
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                return i
        else:
            return 0
			
# Binary Search
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        
        while left < right-1:
            mid=int((left+right)/2)
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid+1]>arr[mid]:
                left=mid+1
            else:
                right=mid-1
            
        
        return left if arr[left]>=arr[right] else right
'''
#Trick is that if arr[mid] is greater than arr[mid+1], then we can say that peak will be on left somewhere since the array.
Else the peak will be on right somewhere
Imagine a mountain with all the points on it and visualize the graph.
'''