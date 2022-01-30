class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        i=0
        while i < (len(colors)):
            j=i+1
            temp_sum=max_sum=neededTime[i]
            while j<len(colors) and colors[j]==colors[i]:
                temp_sum+=neededTime[j]
                max_sum=max(neededTime[j],max_sum)
                j+=1
            time+=(temp_sum-max_sum)
            i=j
        return time
###############################
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        i=1
        temp_sum,max_sum=neededTime[0],neededTime[0]
        while i < (len(colors)):
            if colors[i]==colors[i-1]:
                temp_sum+=neededTime[i]
                max_sum=max(neededTime[i],max_sum)
            else:
                time+=(temp_sum-max_sum)
                temp_sum,max_sum=neededTime[i],neededTime[i]
            i+=1
        time+=(temp_sum-max_sum)
        return time

###############
 def minCost(self, s, cost):
        res = max_cost = 0
        for i in xrange(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res