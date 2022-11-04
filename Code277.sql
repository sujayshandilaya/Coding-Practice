
with cte1 AS
(
Select Server_id, session_status, 
lead(status_time,1) over(order by server_id,status_time) as end_time, 
status_time as start_time
from server_utilization  
)

Select  round(sum (extract(epoch from (end_time-start_time))/(60*60*24)),0)
from cte1 where session_status='start'