
Select 
 case when month <=9 then concat(year,'-','0',month)
 else concat(year,'-',month) end,
 (val+lag1+lag2)/3
from
(
select extract(year from created_at) as year, extract(month from created_at) as month, 
sum(purchase_amt) as val, 
lag(sum(purchase_amt),1) over( order by extract(year from created_at), extract(month from created_at) ) as lag1, 
lag(sum(purchase_amt),2) over( order by extract(year from created_at), extract(month from created_at) ) as lag2
from amazon_purchases where purchase_amt>=0 group by 1,2
)tbl1