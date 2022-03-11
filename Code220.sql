SELECT C.NAME AS country
FROM   country C
       INNER JOIN person P
               ON c.country_code = Substring(P.phone_number, 1, 3)
       INNER JOIN calls C1
               ON P.id = C1.caller_id
                   OR P.id = C1.callee_id
GROUP  BY C.NAME
HAVING Avg(C1.duration) > (SELECT Avg(duration)
                           FROM   calls) 

#############
# Write your MySQL query statement below
WITH cte
     AS (SELECT caller_id AS id,
                duration
         FROM   calls
         UNION ALL
         SELECT callee_id AS id,
                duration
         FROM   calls),
     cte2
     AS (SELECT c.id,
                Substring_index(phone_number, '-', 1) AS code,
                duration
         FROM   person P
                INNER JOIN cte c
                        ON P.id = c.id)
SELECT NAME AS country
FROM   country c
       INNER JOIN (SELECT code
                   FROM   cte2
                   GROUP  BY code
                   HAVING Avg(duration) > (SELECT Avg(duration)
                                           FROM   calls))t1
               ON t1.code = c.country_code  