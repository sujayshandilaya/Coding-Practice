with cte1 as(
SELECT 
extract(year from transaction_Date) as year,
product_id, sum(spend) as curr_year_spend
--over (partition by product_id,extract(year from transaction_Date) order by extract(year from transaction_Date)  )
FROM user_transactions
group by 1,2)

Select year, product_id, curr_year_spend, prev_year_spend,
Round((curr_year_spend - prev_year_spend)*100/prev_year_spend,2) as yoy_rate
from(
Select year, product_id, curr_year_spend, 
lag(curr_year_spend,1) over(partition by product_id order by product_id,year) as prev_year_spend 
from cte1
)t1