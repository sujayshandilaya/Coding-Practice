class Solution:
    def searchRange(self, N: List[int], T: int) -> List[int]:
       
        def find( N: List[int], T, left=0) -> int :
            right=len(N)-1
            while(left<=right):
                mid = left + right >> 1
            
                if N[mid]<T : left=mid+1
                else : right=mid-1
        
            return left
    
        num=find(N,T)
        print(num)
        if num==len(N) or N[num]!=T : return [-1,-1]
        
        return[num, find(N, T+1,num)-1]

