class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums),2):
            temp=[nums[i+1]]*nums[i]
            res+=temp
        
        return res