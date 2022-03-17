SELECT t1.customer_id,
       P.product_id,
       P.product_name
FROM   products P
       INNER JOIN (SELECT customer_id,
                          product_id,
                          Rank()
                            OVER(
                              partition BY customer_id
                              ORDER BY Count(product_id) DESC ) rnk
                   FROM   orders
                   GROUP  BY 1,
                             2) t1 using(product_id)
WHERE  t1.rnk = 1 