
class Solution:
    def countNegatives(self, grids: List[List[int]]) -> int:
        cnt=0
        for  grid in grids:
            left=0
            right=len(grid)-1
            count=0
            while left <=right:
                mid=int((left+right)/2)
                
                if grid[mid]<0:
                    count+= (right-mid+1)
                    right=mid-1
                else:
                    left=mid+1
            cnt+=count
        return cnt
		
######
def countNegatives(self, grid):
        return sum(a<0 for i in grid for a in i)

#Thats how we can iterate two dimensional array in one line