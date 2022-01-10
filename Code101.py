class Solution:
    def reformatDate(self, date: str) -> str:
        month_list=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date=date.split(" ")
        
        day=date[0]
        month=date[1]
        year=date[2]
        month=month_list.index(month)+1
        
        if month<10:
            month='0'+str(month)
        
        day=day[:-2]
        if int(day)<10:
            day='0'+str(day)
        
        return '{}-{}-{}'.format(year,month,day)