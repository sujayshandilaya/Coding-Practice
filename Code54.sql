Select user_id, avg(time) from (
select user_id, date(timestamp), extract (epoch from max(timestamp)- min(timestamp)) as time from
(Select user_id, timestamp, action, row_number() over (partition by user_id,date(timestamp) order by  timestamp desc
) rnk from facebook_web_log where action = 'page_load'
union
Select user_id, timestamp, action, row_number() over (partition by user_id,date(timestamp) order by  timestamp 
) rnk from facebook_web_log where action = 'page_exit')tbl where rnk=1 group by 1,2 )tbl2 group by 1  having avg(time) <>0 order by 1

############

Select user_id, avg(session_time) from(
Select t1.user_id, date(t1.timestamp), (min(t2.timestamp) - max(t1.timestamp)) as session_time  
from  facebook_web_log t1 inner join 
 facebook_web_log t2
 on t1.user_id=t2.user_id
 where t1.action='page_load' and t2.action='page_exit'
 and t1.timestamp<t2.timestamp
group by 1,2
) tbl group by 1
