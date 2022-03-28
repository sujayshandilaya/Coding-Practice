# Write your MySQL query statement below

with cte as (Select requester_id as id from RequestAccepted union all Select accepter_id from RequestAccepted )

Select id, count(id) as num from cte group by 1 order by 2 desc limit 1

######################follow-up#########################

with cte as(
Select id, count(id) as num
from
(
Select requester_id as id from RequestAccepted 
union all
Select accepter_id as id from RequestAccepted) t1
group by id)

Select id, num from cte where num=(Select max(num) from cte)

################################################

with cte as (Select id, count(id) as num  
from
(
Select requester_id as id from RequestAccepted 
union all
Select accepter_id as id from RequestAccepted) t1
group by id)

Select id, num from(
Select id, num, rank() over(order by num desc) as rnk from cte)t2 where rnk=1

########################

Select id, num 
from(
Select id, count(id) as num , rank() over(order by count(id) desc) as rnk 
from
(
Select requester_id as id from RequestAccepted 
union all
Select accepter_id as id from RequestAccepted) t1
group by id) t2 where rnk=1