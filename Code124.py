class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        water=capacity
        for i in range(len(plants)):
            if water>=plants[i]:
                steps=steps+1
                water-=plants[i]
            else:
                steps+=((2*i)+1)
                water=capacity-plants[i]
        
        return(steps)
                
        