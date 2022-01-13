with tbl1 as 
(Select max(salary) as sal, department from db_employee e inner join db_dept d on e.department_id=d.id where department in ('marketing', 'engineering') group by 2)

Select abs(t1.sal-t2.sal) from tbl1 t1,tbl1 t2 where t1.department<>t2.department limit 1

------------

with tbl1 as 
(Select max(salary) as sal, department from db_employee e inner join db_dept d on e.department_id=d.id where department in ('marketing', 'engineering') group by 2)

Select abs((Select sal from tbl1 where department='marketing') - (Select sal from tbl1 where department='engineering' ))

---------------

Select max(case when department='marketing' then salary else null end)- 
max(case when department='engineering' then salary else null end) as engineering_sal from db_employee e left join db_dept d on e.department_id=d.ids