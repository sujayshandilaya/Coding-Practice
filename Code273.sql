With cte1 as(
SELECT user_id, song_id, song_plays FROM songs_history
UNION ALL
Select user_id,song_id, count(*) from 
songs_weekly
where (listen_time::date)<='08/04/2022'
group by 1,2)

Select user_id, song_id, sum(song_plays) as song_plays
FROM cte1
group by 1,2 order by 3 desc