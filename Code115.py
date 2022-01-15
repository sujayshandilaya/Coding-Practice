class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code_set=set()
        for word in words:
            code=""
            for letter in word:
                code+= morse[ord(letter)-97]
            code_set.add(code)
        return(len(code_set))