# Write your MySQL query statement below

with cte1 as (Select passenger_id, min(b.arrival_time) as bus_time from passengers p inner join buses b on p.arrival_time<=b.arrival_time group by 1)

Select bus_id, count(passenger_id) as passengers_cnt from buses b left join cte1 c on c.bus_time=b.arrival_time group by 1 order by 1