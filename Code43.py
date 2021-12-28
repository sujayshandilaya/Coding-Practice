class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr=[None]*2*n
        j=0
        for i in range(n):
            arr[j]=nums[i]
            arr[j+1]=nums[i+n]
            j+=2
        return(arr)
        
#Try yo understand o(1) space complexity solution. above solution is o(n)