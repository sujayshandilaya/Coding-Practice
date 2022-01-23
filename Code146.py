class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        add,cnt=0,0
        i,j=0,0
        for j in range(len(arr)):
            add+=arr[j]
            if j>=k-1:
                if int(add/k) >= t:
                    cnt+=1
                add-=arr[i]
                i+=1
        
        return(cnt)
#######
#similar to previous one, but instead of calculating avg again nd again, we just do it once and compare the sum to it. (logic of target)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        
        add,cnt=0,0
        i,j=0,0
        target=(k*t)
        
        for j in range(len(arr)):
            add+=arr[j]
            if j>=k-1:
                if add >= target:
                    cnt+=1
                add-=arr[i]
                i+=1
        return(cnt)