SELECT NAME
FROM   employee
WHERE  id IN (SELECT managerid
              FROM   employee
              GROUP  BY 1
              HAVING Count(*) >= 5) 

#############

SELECT e1.NAME
FROM   employee e1
       INNER JOIN employee e2
               ON e1.id = e2.managerid
GROUP  BY 1
HAVING Count(*) >= 5 