class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position=[0,0]
        for move in moves:
            if move=='U':
                position[0]+=1
            elif move=='D':
                position[0]-=1
            elif move=='R':
                position[1]+=1
            else:
                position[1]-=1
        
        return True if position==[0,0] else False
		
#####################
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt=Counter(moves)
        
        if cnt['U']==cnt['D'] and cnt['L']==cnt['R']:
            return True
        else:
            return False
##############################
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("R")==moves.count("L") and moves.count("U")==moves.count("D")