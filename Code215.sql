# Write your MySQL query statement below

with cte as (Select requester_id as id from RequestAccepted union all Select accepter_id from RequestAccepted )

Select id, count(id) as num from cte group by 1 order by 2 desc limit 1