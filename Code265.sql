with cte1 as (Select team_id, count(*) as cnt from employee group by 1)

Select employee_id, cnt as team_size from employee e inner join cte1 c on c.team_id=e.team_id

##############################

Select employee_id, count(team_id) over(partition by team_id) as team_size  from employee order by 1