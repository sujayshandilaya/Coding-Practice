SELECT order_id
FROM   ordersdetails
GROUP  BY order_id
HAVING Max(quantity) > (SELECT Max(quant)
                        FROM  (SELECT Avg(quantity) AS quant
                               FROM   ordersdetails
                               GROUP  BY order_id)t1) 

#######

#all keyword is important

SELECT order_id
FROM   ordersdetails
GROUP  BY order_id
HAVING Max(quantity) > ALL (SELECT Avg(quantity) AS quant
                            FROM   ordersdetails
                            GROUP  BY order_id) 