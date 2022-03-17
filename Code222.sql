SELECT e1.id,
       e1.month                     AS month,
       ( e1.salary + COALESCE(e2.salary, 0)
         + COALESCE(e3.salary, 0) ) AS salary
FROM   employee E1
       LEFT JOIN employee E2
              ON E1.id = e2.id
                 AND e1.month = e2.month + 1
       LEFT JOIN employee e3
              ON e1.id = e3.id
                 AND e1.month = e3.month + 2
WHERE  e1.month <> (SELECT Max(month)
                    FROM   employee e4
                    WHERE  e4.id = e1.id
                    GROUP  BY id)
ORDER  BY 1,
          2 DESC 