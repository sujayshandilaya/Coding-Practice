/*
1.How many pizzas were ordered?
2.How many unique customer orders were made?
3.How many successful orders were delivered by each runner?
4.How many of each type of pizza was delivered?
5.How many Vegetarian and Meatlovers were ordered by each customer?
6.What was the maximum number of pizzas delivered in a single order?
7.For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
8.How many pizzas were delivered that had both exclusions and extras?
9.What was the total volume of pizzas ordered for each hour of the day?
10.What was the volume of orders for each day of the week?
*/

1.
select count(pizza_id) from customer_orders
2.
select count(distinct(customer_id)) from customer_orders
3. 
select runner_id,count(runner_id) from runner_orders where pickup_time is not null or distance is not null or duration is not null group by 1
4. 
select pizza_id,count(pizza_id) from customer_orders c inner join runner_orders r on c.order_id=r.order_id where r.pickup_time is not null or r.distance is not null or r.duration is not null group by 1

5.
Select customer_id, pizza_name,count(*) from 
(select customer_id, pizza_name from customer_orders c inner join pizza_names p on 
c.pizza_id=p.pizza_id) tbl group by 1,2 order by 1,2

6. 
Select order_id, cnt from
(select c.order_id, count(pizza_id) cnt from customer_orders c inner join runner_orders r on c.order_id=r.order_id where r.pickup_time is not null or r.distance is not null or r.duration is not null group by 1) tbl2 order by cnt desc limit 1

7.
Select customer_id, changed, count(*) from
(
select c.customer_id, case when (exclusions is null or exclusions ='') and (extras is null or extras='') then 'No Change'
						else 'Change'
					end as 'changed' from customer_orders c inner join runner_orders r on c.order_id=r.order_id where r.pickup_time is not null or r.distance is not null or r.duration is not null) tbl group by 1,2 order by 1

8.
select count(pizza_id) from customer_orders c inner join runner_orders r on c.order_id=r.order_id where c.exclusions <> '' and extras <> '' and  (r.pickup_time is not null or r.distance is not null or r.duration is not null)

9.
Select extract(hour from order_time), count(pizza_id) from customer_orders group by 1 order by 1

10.
Select dayofweek((order_time)), count(order_id) from customer_orders group by 1 order by 1