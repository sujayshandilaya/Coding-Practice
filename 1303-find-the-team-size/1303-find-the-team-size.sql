# Write your MySQL query statement below

Select employee_id, count(team_id) over(partition by team_id) as team_size  from employee order by 1