class Solution(object):
    def sortPeople(self, names, heights):
        height_dict={}
        for i in range(len(names)):
            height_dict[heights[i]]=names[i]
        
        return([v for k, v in sorted(height_dict.items(), key=lambda item: item[0], reverse=True)])
		
########################		
class Solution(object):
    def sortPeople(self, names, heights):
        height_dict={}
        for i in range(len(names)):
            height_dict[heights[i]]=names[i]
        heights.sort(reverse=True)  
        return [height_dict[height] for height in heights]
       