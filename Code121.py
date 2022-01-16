class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weaks={}
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            weaks[i]=0
            for j in range(n):
                if mat[i][j]==1:weaks[i]=weaks.get(i)+1
                else: break
        weaks=sorted(weaks, key=weaks.get)
        return(weaks[0:k])
        