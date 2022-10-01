
with cte1 AS (Select age_bucket,activity_type, sum(time_spent) as time
from activities inner join age_breakdown
using(user_id)
where activity_type in ('send','open')
group by 1,2)

Select age_bucket,round((t2*100)/(t1+t2),2) as send_perc,
round((t1*100)/(t1+t2),2) as open_perc
from(
Select age_bucket, 
sum(case when activity_type='open' then time else 0 end) as t1,
sum(case when activity_type='send' then time else 0 end) as t2
from cte1
group by age_bucket)tbl1

##################################

Select age_bucket,
round(sum(case when activity_type='send' then time_spent else 0 end)*100/sum(time_spent),2) as send_perc,
round(sum(case when activity_type='open' then time_spent else 0 end)*100/sum(time_spent),2) as open_perc
from activities inner join age_breakdown
using(user_id)
where activity_type in ('send','open')
group by 1