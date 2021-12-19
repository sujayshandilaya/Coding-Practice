class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_num={}
        
        for i in range(len(nums)):
            if nums[i] in dict_num.keys() and abs(i-dict_num[nums[i]])<=k:
                    return True
            else:
                dict_num[nums[i]]=i               
        return False
                
##########

#Initialize a hashmap and iterate through each index i and value v in enumerate(nums).
#If v exists as a key in hashmap and the difference between the current index and the value of the existing index in the hashmp is at most k, then return True
#If v does not exist as a key in hashmap, add it as hashmap[v] = i
#If we reach the end of iteration, return False

#i is index and v is value

#enumerate returns a dictinary with index,value form

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
	hashmap = {}
	for i,v in enumerate(nums):
		if v in hashmap and i - hashmap[v] <= k:
			return True
		hashmap[v] = i
	return False