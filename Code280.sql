Select user_id, max(lead_date) as biggest_window
from
(Select user_id, datediff(lead(visit_date,1,'2021-01-01') over(partition by user_id order by visit_date),visit_date) as lead_date 
from UserVisits)t1
group by 1