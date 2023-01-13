SELECT transaction_date, user_id, cnt
from
(SELECT transaction_date, user_id, count(product_id) as cnt, 
row_number() over(partition by user_id order by transaction_date desc) as rnum
from user_transactions
group by 1,2)t1
where rnum=1
order by transaction_date