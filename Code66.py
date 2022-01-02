class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operation=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if (boxes[j]=='1'):
                    operation[i]=operation[i]+abs(i-j)
            
            
        return(operation)


class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)

        right_dist=[0]*n
        left_dist=[0]*n
        result=[0]*n
        left_cnt=int(boxes[0])
        
        for i in range(1,n):
            left_dist[i]=left_dist[i-1]+left_cnt
            left_cnt+=int(boxes[i])
        
        right_cnt=int(boxes[n-1])
        
        for i in range(n-2,-1,-1):
            right_dist[i]=right_dist[i+1]+right_cnt
            right_cnt+=int(boxes[i])
        
        for i in range(n):
            result[i]=left_dist[i]+right_dist[i]
        #print(left_dist[2], right_dist[2])    
        return(result)
            