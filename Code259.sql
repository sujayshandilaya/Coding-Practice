with cte1 AS
(
Select s.artist_id, count(*), dense_rank() over(order by count(*) desc) as dsr
from songs s 
inner join
global_song_rank gsr 
on s.song_id=gsr.song_id
where gsr.rank<=10
group by s.artist_id
)

Select artist_name, dsr as artist_rank
from artists a inner join cte1 c1
on a.artist_id=c1.artist_id
where dsr<=5
order by dsr, artist_name