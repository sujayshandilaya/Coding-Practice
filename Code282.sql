Select company, sp from
(
select company, sum(profits) as sp, rank() over(order by sum(profits) desc) as rnk  from forbes_global_2010_2014
group by 1) t1 where rnk<=3


################

select company, sum(profits) as sp from forbes_global_2010_2014
group by 1 order by 2 desc limit 3;