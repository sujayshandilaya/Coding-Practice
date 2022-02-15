class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt=0
        count_dict={}
        for t in time:
            rem=t%60
            cnt+=count_dict.get(60-rem,0)
            if rem!=0:
                count_dict[rem]=count_dict.get(rem,0)+1
            else:
                count_dict[60]=count_dict.get(60,0)+1
        return cnt

#############################
"""
This is problem is similar to the Two Sum problem, but with a slight modular twist.
So, here we need to find a and b such that (a + b) % 60 == 0. This can be also written as,
=> (a % 60) + (b % 60) == 60
=> (a % 60) == 60 - (b % 60)

So if both reminder ads up to 60 we can tell it is indeed a valid pair of songs. One, edge case which we have to keep in mind is, what if (a % 60) = 0 and (b % 60) = 0 our result will be 0 + 0 = 0, this fails our intution. So to handle this case we can rewrite the equation as
=> (a % 60) == (60 - (b % 60)) % 60

BTW, Talking is cheap, so here we go : )
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # array which keep count of no of occurences of reminders
        dp = [0]*60
        res = 0
        for t in time:
            rem = t % 60
            target = (60 - rem) % 60
            res += dp[target]
            dp[rem] += 1
        return res