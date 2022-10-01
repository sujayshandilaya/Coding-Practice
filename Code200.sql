Select a1.player_id, a1.event_date, sum(a2.games_played) as games_played_so_far from 
Activity a1 inner join Activity a2 
on a1.player_id = a2.player_id and a1.event_date >= a2.event_date
group by 1,2
order by 1

#################

SELECT 
player_id, event_date,
sum(games_played) over( partition by player_id order by event_date rows between unbounded preceding and current row) as games_played_so_far from 
Activity

###################

select 
    player_id,
    event_date,
    sum(games_played) over
    (partition by player_id order by event_date asc) AS games_played_so_far
from 
    activity