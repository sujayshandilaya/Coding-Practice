# Write your MySQL query statement below

with t1 as (Select distinct product_id from Products)

,t2 as( 

Select product_id, new_price from
(
Select product_id, new_price, change_date, date_sub(lead(change_date, 1 , '3000-01-01') over(partition by product_id order by change_date), Interval 1 day) as new_date from Products ) t where change_date<='2019-08-16' and new_date>='2019-08-16'
)

Select t1.product_id, coalesce(new_price,10)  as price
from
t1 left join t2 using(product_id) #where change_date<='2019-08-16' and new_date>'2019-08-16'