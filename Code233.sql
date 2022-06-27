# Write your MySQL query statement below
 with cte1 as
 (Select host_team as team_id, case when host_goals>guest_goals then 3 when host_goals=guest_goals then 1 else 0 end as points from Matches
 
  union all
  
  select guest_team as team_id, case when host_goals>guest_goals then 0 when host_goals=guest_goals then 1 else 3 end as points from Matches
  
 )
 , cte2 as( 
 Select team_id, sum(points) as points from cte1 group by 1
     )
     
  SELECT t.team_id,t.team_name, coalesce(c.points,0) as num_points from Teams t left join cte2 c on t.team_id=c.team_id order by num_points desc,team_id   