Select user_id, avg(time) from (
select user_id, date(timestamp), extract (epoch from max(timestamp)- min(timestamp)) as time from
(Select user_id, timestamp, action, row_number() over (partition by user_id,date(timestamp) order by  timestamp desc
) rnk from facebook_web_log where action = 'page_load'
union
Select user_id, timestamp, action, row_number() over (partition by user_id,date(timestamp) order by  timestamp 
) rnk from facebook_web_log where action = 'page_exit')tbl where rnk=1 group by 1,2 )tbl2 group by 1  having avg(time) <>0 order by 1