CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
      Select 
      avg(salary) as SecondHighestSalary from (Select salary, dense_rank() over(order by salary desc) rnk from Employee)t1 where rnk=N
      
  );
END

#aggregate function is used to return null incase the returned string is empty.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      # Write your MySQL query statement below
      SELECT max(Salary) 
from
(
SELECT distinct Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 offset N
)tbl1
      
  );
END

#offset doesnt consider the first N rows and considers only the remaining rows.