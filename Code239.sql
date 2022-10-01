with cte1 as (
SELECT title, avg(salary) as avg_salary 
FROM employee_pay group by 1
)

Select employee_id, salary, status
from 
(Select e.employee_id, e.salary, 
case when salary > 2*avg_salary then 'Overpaid'
when salary < avg_salary/2 then 'Underpaid'
else null end as status FROM
employee_pay e inner join cte1 using(title)
)t1 where status is not null


############################

Select employee_id, salary, status
from 
(Select e.employee_id, e.salary, 
case when salary > 2*avg_salary then 'Overpaid'
when salary < avg_salary/2 then 'Underpaid'
else null end as status from
(Select *, AVG(salary) over(partition by title) as avg_salary
from employee_pay) e
) t1 where status is not null