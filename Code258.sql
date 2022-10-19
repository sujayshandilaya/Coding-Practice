with cte1 as(
SELECT category, product, sum(spend) as total_spend
FROM product_spend
where EXTRACT(year from transaction_date)=2022
group by 1,2)

Select category, product, total_spend
from
(
Select category, product, total_spend,
RANK() over(partition by category order by total_spend desc) as rnk_spend
from cte1
) t1 where rnk_spend<=2

#############

with cte1 as(
SELECT category, product, sum(spend) as total_spend,
RANK() over(partition by category order by sum(spend) desc) as rnk_spend
FROM product_spend
where EXTRACT(year from transaction_date)=2022
group by category, product
)

Select category, product, total_spend
from cte1 where rnk_spend<=2
