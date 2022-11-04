# Write your MySQL query statement below

Select c.name as country
from
(Select Caller_id as caller, duration from Calls
union all
Select callee_id as caller, duration from calls) t1
inner join
Person p
on p.id=t1.caller
inner join Country c
on left(phone_number,3) = c.country_code
group by 1
having avg(duration) > (Select avg(duration) from Calls)