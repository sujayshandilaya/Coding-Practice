class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        c=Counter(nums)
        res=[]
        freq_count=[0]*k
        
        for count in c.values():
            minimum=min(freq_count)
            if count>minimum:
                freq_count.remove(minimum)
                freq_count.append(count)
            
        for key,value in c.items():
            if value in freq_count:
                res.append(key)
        
        return res
        
 #############
 
 class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sorted(d, key=d.get, reverse=True)[:k]
            
        
  ###################
  
  class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums) 
        return sorted(d, key=d.get, reverse=True)[:k]