with cte as (Select stock_name, operation, sum(price) as sp from Stocks group by 1,2)

Select stock_name, capital_gain_loss 
from
(Select stock_name, sp-lag(sp) over (partition by stock_name order by operation desc ) as capital_gain_loss from cte) tbl1 
where capital_gain_loss is not null

############


with buy as (Select stock_name, sum(price) as sp from Stocks where operation="Buy" group by 1),

sell as (Select stock_name, sum(price) as sp from Stocks where operation="Sell" group by 1)

Select tbl1.stock_name, (tbl2.sp-tbl1.sp) as capital_gain_loss from buy tbl1 inner join sell tbl2 on tbl1.stock_name= tbl2.stock_name