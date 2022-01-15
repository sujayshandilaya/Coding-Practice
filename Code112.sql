select id,first_name,last_name, department_id, salary from (select id,first_name,last_name, department_id, salary , rank() over ( partition by id order by salary desc) rnk from ms_employee_salary) tbl1 where rnk=1 order by 1

-----------
select id,first_name,last_name, department_id, max(salary) from ms_employee_salary group by 1,2,3,4
order by 1