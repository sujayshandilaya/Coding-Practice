class Solution:
    def isValidSudoku(self, boards: List[List[str]]) -> bool:
        
        def containDuplicate(nums:List[str])->bool:
            set_dup=set()
            for ele in nums:
                if ele==".":
                    pass
                else:
                
                    if ele in set_dup:
                        return False
                    else :
                        set_dup.add(ele)
            return True
        
        dict_list={0:[],
				   1:[],
				   2:[],
				   3:[],
				   4:[],
				   5:[],
				   6:[],
				   7:[],
				   8:[]}

        
        for board in boards:
            res=containDuplicate(board)
            if res==False: 
                return False
        
        for i in range(9):
            li=[board[i] for board in boards]
            res=containDuplicate(li)
            if res==False:
                return False
        
        for i in range(9):
            for j in range(9):
                Sr=int(i/3)
                Sc=int(j/3)
                R=(Sr*3)+Sc 
                dict_list[R].append(boards[i][j])
                
        for i in range(9):
            li=dict_list.get(i)
            res=containDuplicate(li)
            if res==False:
                return False
        
        return True
        
############### Same solution with less if else

class Solution:
    def isValidSudoku(self, boards: List[List[str]]) -> bool:
        
        def containDuplicate(nums:List[str])->bool:
            set_dup=set()
            for ele in nums:
                if ele==".":
                    pass
                else:
                
                    if ele in set_dup:
                        return False
                    else :
                        set_dup.add(ele)
            return True
        
        dict_list={0:[],
                    1:[],
                    2:[],
                    3:[],
                    4:[],
                    5:[],
                    6:[],
                    7:[],
                    8:[]}

        
        for i in range(9):
            if containDuplicate(boards[i]) is False: return False
			
            li=[board[i] for board in boards]
            if containDuplicate(li) is False: return False

            for j in range(9):
                Sr=int(i/3)
                Sc=int(j/3)
                R=(Sr*3)+Sc 
                dict_list[R].append(boards[i][j])
                
        for i in range(9):
            li=dict_list.get(i)
            if containDuplicate(li) is False: return False
        
        return True