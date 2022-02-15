Select t1.id, t1.company, salary from

 (
 SELECT   id,
          company,
          salary,
          Row_number() OVER(partition BY company ORDER BY salary ) AS rnum
 FROM     employee) t1 INNER JOIN
(
         SELECT   company,
                  count(*) AS cnt
         FROM     employee
         GROUP BY 1) t2 ON t1.company=t2.company
AND
(
  t1.rnum IN
  (
         SELECT
                CASE
                       WHEN cnt%2=0 THEN (cnt/2)
                       ELSE (cnt+1)/2
                END)
  OR
  t1.rnum =
  (
         SELECT
                CASE
                       WHEN cnt%2=0 THEN (cnt/2)+1
                       ELSE (cnt+1)/2
                END)
)

##########################


with cte as (Select id, company, salary, row_number() over(partition by company order by salary) rnk, count(id) over(partition by company) as cnt from Employee)

Select id, company, salary from cte where rnk between cnt/2.0 and cnt/2.0 +1