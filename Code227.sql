# Write your MySQL query statement below
SELECT s.user_id,
       Coalesce(t1.confirmation_rate, 0.00) AS confirmation_rate
FROM   signups s
       LEFT JOIN (SELECT user_id,
                         Round(Sum(CASE
                                     WHEN action = 'confirmed' THEN 1
                                     ELSE 0
                                   end) / Count(action), 2) AS confirmation_rate
                  FROM   confirmations
                  GROUP  BY 1) t1
              ON s.user_id = t1.user_id 

##################

# Write your MySQL query statement below

Select s.user_id, coalesce(t1.confirmation_rate,0.00) as confirmation_rate from Signups s 
left join 
(
Select user_id, round(avg(action='confirmed'),2) as confirmation_rate From Confirmations group by 1) t1 on s.user_id=t1.user_id