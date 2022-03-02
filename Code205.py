class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes= sorted(boxTypes, key = lambda x: x[1], reverse=True)
        occupied=op=0
        for box in boxTypes:
            if (occupied+box[0]) > truckSize:
                op+=((truckSize-occupied)*box[1])
                break
            else:
                occupied+=box[0]
                op+=(box[0]*box[1])
        
        return op
            