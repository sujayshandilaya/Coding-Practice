WITH cte
     AS (SELECT s.buyer_id,
                p.product_name
         FROM   sales s
                INNER JOIN product p using(product_id)
         WHERE  product_name IN ( 'S8', 'iPhone' )
         GROUP  BY 1,
                   2)
SELECT buyer_id
FROM   cte
WHERE  product_name = 'S8'
       AND buyer_id NOT IN (SELECT buyer_id
                            FROM   cte
                            WHERE  product_name = 'iPhone') 

##################

SELECT s.buyer_id
FROM   sales s
       INNER JOIN product p using(product_id)
WHERE  p.product_name IN ( 'S8', 'iPhone' )
GROUP  BY 1
HAVING Sum(p.product_name = "S8") > 0
       AND Sum(p.product_name = "iPhone") = 0 