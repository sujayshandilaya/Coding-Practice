# Write your MySQL query statement below
SELECT Round(Count(a1.player_id) / (SELECT Count(DISTINCT player_id)
                                    FROM   activity), 2) AS fraction
FROM   (SELECT player_id,
               Min(event_date) AS event_date
        FROM   activity
        GROUP  BY 1) a1
       INNER JOIN activity a2
               ON a1.player_id = a2.player_id
                  AND a1.event_date = Date_sub(a2.event_date, INTERVAL 1 day) 