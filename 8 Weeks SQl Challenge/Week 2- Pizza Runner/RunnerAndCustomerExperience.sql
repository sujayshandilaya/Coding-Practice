/*
1.How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)
2.What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order?
3.Is there any relationship between the number of pizzas and how long the order takes to prepare?
4.What was the average distance travelled for each customer?
5.What was the difference between the longest and shortest delivery times for all orders?
6.What was the average speed for each runner for each delivery and do you notice any trend for these values?
7.What is the successful delivery percentage for each runner?
*/

1.
SELECT week(registration_date, week('2021-01-01')+1)+1 as week_no, count(runner_id) from runners group by 1;

2.

SELECT runner_id, avg(TIMESTAMPDIFF(MINUTE, order_time, pickup_time)) from customer_orders c 
inner join runner_orders r 
on r.order_id=c.order_id 
where pickup_time is not null
group by 1 order by 1

3.

4.

