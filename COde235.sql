Select product_name , product_id, order_id, order_date
from
(Select product_name , o.product_id, order_id, order_date, rank() over(partition by product_id order by order_date desc) rnk from Orders o inner join Products p using(product_id) ) tbl1 where rnk=1 order by product_name, product_id, order_id