# Write your MySQL query statement below
with cte as (Select business_id, event_type, occurences, avg(occurences) over(partition by event_type) as avg_ocur from Events)

Select business_id 
from
(
Select business_id, sum(case when occurences> avg_ocur then 1 else 0 end) as cnt from  cte group by 1)t1 where cnt>=2