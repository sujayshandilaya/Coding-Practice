class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money=0
        for i in accounts:
            max_money=max(sum(j for j in i),max_money)
        return max_money
		

###############

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money=max([sum(i) for i in accounts])
        return(max_money) 

####################

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money=max(sum(i) for i in accounts)
        return(max_money) 


#####################

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money=max(map(sum, accounts))
        return(max_money)              

#map function maps a function to an iterator and it returns an iterator.