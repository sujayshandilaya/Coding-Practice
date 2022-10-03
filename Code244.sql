with cte1 as(
SELECT user_id, tweet_date, count(*) as cnt
FROM tweets
group by 1,2 )

Select user_id, tweet_date, 
round(avg(cnt) over(PARTITION BY user_id order by tweet_date 
rows between 2 preceding and current row),2) as rolling_avg_3days
from cte1