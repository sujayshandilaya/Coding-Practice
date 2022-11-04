with cte1 as
(Select (transaction_date::date), 
sum(case when type ='deposit' then amount else -1*amount end) as balance
from transactions 
group by 1)

Select transaction_date, 
sum(balance) over(PARTITION BY extract(month from transaction_date) order by transaction_date)
from cte1