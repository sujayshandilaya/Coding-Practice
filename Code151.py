class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        n=len(grumpy)
        satisfied=sum([customers[i]*(1-grumpy[i]) for i in range(n)])
        max_satisfied=satisfied
        for i in range(n):
            if grumpy[i]==1: satisfied+=customers[i]    
            if i>=minutes:
                if grumpy[i-minutes]==1: satisfied-=customers[i-minutes]
            max_satisfied=max(satisfied,max_satisfied)
        return max_satisfied