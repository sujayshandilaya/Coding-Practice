with avg_dept as (select department, avg(salary) as avg_sal from employee group by 1)

Select e.department, e.first_name,e.salary,ad.avg_sal
from employee e inner join avg_dept ad
on e.department=ad.department

#######################


Select e.department, e.first_name,e.salary,avg(salary) over (partition by department)
from employee e 