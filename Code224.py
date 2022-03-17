class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted(x[0] for x in intervals)
        end=sorted(x[1] for x in intervals)
        s=e=0
        num_rooms=available=0
        while s<len(start):
            if start[s]<end[e]:
                if available==0:
                    num_rooms+=1
                else:
                    available-=1
                s+=1
            else:
                available+=1
                e+=1
        return num_rooms
