class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        minimum=[]
        li=[]
        
        for rows in matrix:
            minimum.append(min(rows))
        
        for i in range(len(matrix[0])):
            num=max([rows[i] for rows in matrix])
            if num in minimum:
                li.append(num)
        
        return li
		
#################
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minimum=[]
        li=[]
        for rows in matrix:
            minimum.append(min(rows))
        for col in zip(*matrix):
            num=max(col)
            if num in minimum:
                li.append(num)
        
        return li

Zip(*matrix):

if [[1,2][3,4]]