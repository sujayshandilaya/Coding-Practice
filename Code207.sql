# Write your MySQL query statement below

with tbl as (SELECT 1 as num union all
SELECT 2 as num union all
SELECT 3 as num union all
SELECT 4 as num union all
SELECT 5 as num union all
SELECT 6 as num union all
SELECT 7 as num union all
SELECT 8 as num union all
SELECT 9 as num union all
SELECT 10 as num  union all
SELECT 11 as num union all
SELECT 12 as num union all
SELECT 13 as num union all
SELECT 14 as num union all
SELECT 15 as num union all
SELECT 16 as num union all
SELECT 17 as num union all
SELECT 18 as num union all
SELECT 19 as num union all
SELECT 20 as num
),

 tbl1 as ( Select T.task_id, c.num  as subtask_id from Tasks T,tbl c where c.num<=T.subtasks_count)


Select T.task_id, T.subtask_id from tbl1 T left join Executed E on E.task_id=T.task_id and E.subtask_id=T.subtask_id where E.subtask_id is null order by 1,2