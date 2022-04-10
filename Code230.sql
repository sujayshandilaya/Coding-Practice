SELECT Round(Avg(order_date = customer_pref_delivery_date) * 100, 2) AS
       immediate_percentage
FROM  (SELECT customer_id,
              order_date,
              customer_pref_delivery_date,
              Row_number()
                OVER(
                  partition BY customer_id
                  ORDER BY order_date)rnum
       FROM   delivery)t1
WHERE  rnum = 1 

###############

SELECT Round(Avg(order_date = customer_pref_delivery_date) * 100, 2) AS
       immediate_percentage
FROM   delivery
WHERE  ( customer_id, order_date ) IN (SELECT customer_id,
                                              Min(order_date)
                                       FROM   delivery
                                       GROUP  BY 1) 