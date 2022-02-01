class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l1={
            'row':[],
            'col':[]
           }
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l1['row']+=[i]
                    l1['col']+=[j]

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])):
                if i in l1['row'] or j in l1['col']:
                    matrix[i][j]=0
  
  
  class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r1=c1=-1
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
                    if i==0:
                        r1=0
                    if j==0:
                        c1=0

        print(matrix)
        for i in range(1,len(matrix)) :
            for j in range(1,len(matrix[0])):
                    matrix[i][j]=0 if matrix[0][j]==0 or matrix[i][0]==0 else matrix[i][j]
        
        if r1==0:
            print("insied r1")
            for j in range(0,len(matrix[0])):
                matrix[0][j]=0
        if c1==0:
            print("insied c1")
            for i in range(0,len(matrix)):
                matrix[i][0]=0
  