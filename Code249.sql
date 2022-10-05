Select cnt as tweet_bucket, count(cnt) as users_num
from
(SELECT 
user_id, count(msg) as cnt
FROM tweets
where extract(year from tweet_date)=2022
group by 1) t1
group by 1;