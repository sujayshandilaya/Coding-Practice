# Write your MySQL query statement below
  Select s1.gender, s1.day, sum(s2.score_points) as total
  from scores s1 inner join scores s2
  on s1.gender=s2.gender and s1.day>=s2.day
  group by 1,2
  order by 1,2