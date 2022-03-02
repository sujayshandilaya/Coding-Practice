WITH tbl
     AS (SELECT 1 AS num
         UNION ALL
         SELECT 2 AS num
         UNION ALL
         SELECT 3 AS num
         UNION ALL
         SELECT 4 AS num
         UNION ALL
         SELECT 5 AS num
         UNION ALL
         SELECT 6 AS num
         UNION ALL
         SELECT 7 AS num
         UNION ALL
         SELECT 8 AS num
         UNION ALL
         SELECT 9 AS num
         UNION ALL
         SELECT 10 AS num
         UNION ALL
         SELECT 11 AS num
         UNION ALL
         SELECT 12 AS num
         UNION ALL
         SELECT 13 AS num
         UNION ALL
         SELECT 14 AS num
         UNION ALL
         SELECT 15 AS num
         UNION ALL
         SELECT 16 AS num
         UNION ALL
         SELECT 17 AS num
         UNION ALL
         SELECT 18 AS num
         UNION ALL
         SELECT 19 AS num
         UNION ALL
         SELECT 20 AS num),
     tbl1
     AS (SELECT T.task_id,
                c.num AS subtask_id
         FROM   tasks T,
                tbl c
         WHERE  c.num <= T.subtasks_count)
SELECT T.task_id,
       T.subtask_id
FROM   tbl1 T
       LEFT JOIN executed E
              ON E.task_id = T.task_id
                 AND E.subtask_id = T.subtask_id
WHERE  E.subtask_id IS NULL
ORDER  BY 1,
          2 

################################

WITH recursive tbl AS
(
       SELECT 1 AS num
       UNION ALL
       SELECT num+1
       FROM   tbl
       WHERE  num < 20 ), tbl1 AS
(
       SELECT t.task_id,
              c.num AS subtask_id
       FROM   tasks t,
              tbl c
       WHERE  c.num<=t.subtasks_count)
SELECT    t.task_id,
          t.subtask_id
FROM      tbl1 t
LEFT JOIN executed e
ON        e.task_id=t.task_id
AND       e.subtask_id=t.subtask_id
WHERE     e.subtask_id IS NULL


###################################


WITH recursive tbl AS
(
         SELECT   task_id,
                  1 AS num
         FROM     tasks
         GROUP BY 1
         UNION ALL
         SELECT task_id ,
                num+1
         FROM   tbl t1
         WHERE  num <
                (
                       SELECT subtasks_count
                       FROM   tasks t
                       WHERE  t.task_id=t1.task_id) )
SELECT    t.task_id,
          t.num AS subtask_id
FROM      tbl t
LEFT JOIN executed e
ON        e.task_id=t.task_id
AND       e.subtask_id=t.num
WHERE     e.subtask_id IS NULL
