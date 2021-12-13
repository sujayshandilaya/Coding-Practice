class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_strip= s.rstrip()
        words=s_strip.split(" ")
        return(len(words[-1]))
