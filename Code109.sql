select worker_title from worker inner join title on worker.worker_id=title.worker_ref_id where salary = (Select max(salary) from worker) ;
------
SELECT *
FROM
  (SELECT CASE
              WHEN salary =
                     (SELECT max(salary)
                      FROM worker) THEN worker_title
          END AS best_paid_title
         
   FROM worker a
   INNER JOIN title b ON b.worker_ref_id=a.worker_id
   ORDER BY best_paid_title) sq
WHERE best_paid_title IS NOT NULL