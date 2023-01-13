# Write your MySQL query statement below
Select activity from(

Select activity, count(*) as cnt, 
rank() over(order by count(*) desc) as r1, 
rank() over(order by count(*)) as r2 from Friends group by 1

)t1 where r2<> 1 and r1<>1
