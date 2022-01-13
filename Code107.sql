-- Join
Select e1.name as Employee from employee e1 inner join employee e2 on e2.id=e1.managerid where e1.salary > e2.salary

--Subquery

Select e.name as Employee from employee e
where e.salary > (Select m.salary from employee m where e.managerid=m.id)

--Join is faster than subquery
-- subquery is easier to understand and follows the logical steps.