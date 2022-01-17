Select max(salary) as SecondHighestSalary from (Select salary, dense_rank() over(order by salary desc) rnk from Employee)t1 where rnk=2

Select max(salary) as SecondHighestSalary  from Employee where salary <>(Select max(salary) from Employee )

SELECT max(Salary) AS SecondHighestSalary
from
(
SELECT distinct Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 offset 1
)tbl1


The OFFSET clause specifies the number of rows to skip before starting to return rows from the query