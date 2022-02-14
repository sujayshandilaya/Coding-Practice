class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_final=0
        for i in range(len(prices)):
            profit = max(j for j in prices[i:])-prices[i]
            profit_final=max(profit,profit_final)      
        return(profit_final)
###############

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_final,minimum=0,prices[0]
        for i in range(1,len(prices)):
            if prices[i]>minimum: profit_final=max(profit_final,(prices[i]-minimum))  
            else: minimum=prices[i]
        return profit_final