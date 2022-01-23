Select d.name as Department, tbl1.name as Employee, tbl1.salary as Salary from
Department D inner join
(
select name, salary, departmentId from Employee e where salary = (Select max(Salary) from Employee e1 where e1.departmentId=e.departmentId) ) tbl1 on tbl1.departmentId = D.id

###########

Select d.name as Department, tbl1.name as Employee, tbl1.salary as Salary from
Department D inner join
(
Select name, salary, departmentId, rank() over ( partition by departmentId order by salary desc) rnk from Employee) tbl1
on
tbl1.departmentId = D.id where tbl1.rnk=1