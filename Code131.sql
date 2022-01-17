Select distinct l1.num as ConsecutiveNums from Logs l1, Logs l2, Logs L3 where l1.id+1 = l2.id and l2.id+1=l3.id and l1.num=l2.num and l2.num=l3.num

##############

Select distinct(num) as ConsecutiveNums 
from
(Select num, lag(num) over (order by id) as prev1, lead(num) over(order by id) as next1 from Logs) tbl1  where num=prev1 and num=next1

--cross join would be more efficient for small tables, for large no of records, it would be inefficient.

--Hence, we use lead and lag for large no of records, but for small records use cross join method

