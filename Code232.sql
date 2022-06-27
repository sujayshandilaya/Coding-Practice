with vol_cte as
(Select product_id, (width*length*height) as vol from Products)

Select name as warehouse_name, sum(units*vol) as volume from Warehouse w inner join vol_cte v on  w.product_id=v.product_id group by 1

############

Select name as warehouse_name, sum(units*width*length*height) as volume from Warehouse w inner join Products p on  w.product_id=p.product_id group by 1