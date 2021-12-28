class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies=max(candies)
        
        for i in range(len(candies)):
            candies[i]= True if candies[i]+extraCandies>= maxCandies else False
        
        return(candies)
 #######
 class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies=max(candies)
        
        diff = maxCandies-extraCandies
        
        return[diff<=candy for candy in candies]