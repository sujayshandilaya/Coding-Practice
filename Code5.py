class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000 }
        num=0
        i=0
        while (i < len(s)):
            if(i!=len(s)-1 and roman_dict[s[i]]<roman_dict[s[i+1]]):
                num=num+(roman_dict[s[i+1]]-roman_dict[s[i]])
                i+=2
            else:
                num=num+roman_dict[s[i]]
                i+=1
        return(num)

############

class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number