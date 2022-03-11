WITH cte
     AS (SELECT NAME
         FROM   (SELECT O.sales_id
                 FROM   orders O
                        INNER JOIN (SELECT com_id
                                    FROM   company
                                    WHERE  NAME = "red")t1
                                ON t1.com_id = O.com_id) t2
                INNER JOIN salesperson S
                        ON S.sales_id = t2.sales_id)
SELECT NAME
FROM   salesperson
WHERE  NAME NOT IN (SELECT *
                    FROM   cte) 
					
################


SELECT NAME
FROM   salesperson s
       LEFT JOIN (SELECT sales_id
                  FROM   orders O
                         INNER JOIN company C
                                 ON C.com_id = O.com_id
                  WHERE  C.NAME = "red") t1
              ON s.sales_id = t1.sales_id
WHERE  t1.sales_id IS NULL 