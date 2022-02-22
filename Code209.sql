# Write your MySQL query statement below
SELECT Round(Coalesce(accepted / sent, 0), 2) AS accept_rate
FROM   (SELECT Count(DISTINCT( Concat(requester_id, accepter_id) )) AS accepted
        FROM   requestaccepted) t1,
       (SELECT Count(DISTINCT( Concat(sender_id, send_to_id) )) AS sent
        FROM   friendrequest) t2 
		

SELECT Round(COALESCE(accepted / sent, 0), 2) AS accept_rate
FROM   (SELECT Count(DISTINCT requester_id, accepter_id) AS accepted
        FROM   requestaccepted) t1,
       (SELECT Count(DISTINCT sender_id, send_to_id) AS sent
        FROM   friendrequest) t2 


SELECT Round(COALESCE((SELECT Count(DISTINCT requester_id, accepter_id) /
                              Count(DISTINCT sender_id,
                              send_to_id)
                       FROM   requestaccepted,
                              friendrequest), 0), 2) AS accept_rate 