Select gender,day, sum(score_points) over(partition by gender order by day) as total from scores
  
###########################################

  Select s1.gender, s1.day, sum(s2.score_points) as total
  from scores s1 inner join scores s2
  on s1.gender=s2.gender and s1.day>=s2.day
  group by 1,2
  order by 1,2

