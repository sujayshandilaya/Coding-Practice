select c.first_name,o.order_date,sum(o.total_order_cost) from customers c inner join orders o on c.id=o.cust_id  where o.order_date between '2019-02-01' and '2019-05-01' group by 1,2 order by 3 desc limit 1;

##########

Select first_name, order_date,total_order from
(Select first_name, order_date,total_order, rank() over (order by total_order desc) as rnk
from
(
select c.first_name,o.order_date,sum(o.total_order_cost) as total_order from customers c inner join orders o on c.id=o.cust_id  where o.order_date between '2019-02-01' and '2019-05-01' group by 1,2
) tbl1
)tbl2 where rnk=1
;
#############
with agg_view as
(
select c.first_name,o.order_date,sum(o.total_order_cost) as total_order from customers c inner join orders o on c.id=o.cust_id  where o.order_date between '2019-02-01' and '2019-05-01' group by 1,2
)
Select * from agg_view where total_order=(Select max(total_order) from agg_view)
;