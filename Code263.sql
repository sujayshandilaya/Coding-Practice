with cte1 as (
Select product_id, category from products where category is not null
),

 cte2 AS
(
Select p.product_id,p.name, max(c.product_id) as new_product from products p  
inner join cte1 c
on p.Product_id>=c.product_id
group by 1,2)

Select cte2.product_id, cte1.category, cte2.name
from cte1 inner join cte2
on cte2.new_product=cte1.product_id
order by 1

#############################

WITH fill_products AS (
SELECT
  product_id,
  category,
  name,
  COUNT(category) OVER (ORDER BY product_id) AS category_group
FROM products)

SELECT
  product_id,
  FIRST_VALUE (category) OVER (
  	PARTITION BY category_group
    ORDER BY product_id) AS category,
  name
FROM fill_products;

###############################################

SELECT
  product_id,first_value(category) 
  over ( partition by category_partition 
  order by product_id)
  as category,name
FROM 
(
    SELECT product_id,
    category,
    name,
    sum(case when category is null then 0 else 1 end) 
    over  (order by product_id) as category_partition
  FROM products
  ORDER BY product_id ASC
) as p

####################

COUNT(category) OVER (ORDER BY product_id) & sum(case when category is null then 0 else 1 end) over  (order by product_id) 

They both can be used to allot a same number to each of the categories.
