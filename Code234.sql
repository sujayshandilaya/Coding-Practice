with cte1 as (Select team_id, count(*) as cnt from employee group by 1)

Select employee_id, cnt  as team_size from Employee inner join cte1 on employee.team_id=cte1.team_id

#####################################

# Write your MySQL query statement below

Select employee_id, count(team_id) OVER(partition by team_id) as team_size from Employee group by 1 order by 1

