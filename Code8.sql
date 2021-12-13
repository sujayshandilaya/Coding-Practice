--Approach1:
select id, case when id%2=1  then lead(student ,1,student) OVER(ORDER BY id)
else lag(student ,1 ) OVER(ORDER BY id) end as student from Seat;

--Approach 2:
-- Write your MySQL query statement below
Select * from
(select tbl1.id, coalesce(tbl2.student, tbl1.student) as student from Seat as tbl1 left join Seat as tbl2 on tbl1.id=(tbl2.id-1) where tbl1.id%2 <> 0
union
select tbl2.id, tbl1.student as student from Seat as tbl1 left join Seat as tbl2 on tbl1.id=(tbl2.id-1) where tbl2.id%2 = 0) xyz order by id;

--Approach 3:
select
dense_rank() over(
order by case when id%2 = 1 then id+1 else id-1 end) as id,
student
from Seat s

--Note: Order by clause can be manipulated using case statements.
--https://www.tech-recipes.com/rx/69861/how-to-use-case-statement-in-order-by-clause/ 
--Window function output is always by ranks assigned.
