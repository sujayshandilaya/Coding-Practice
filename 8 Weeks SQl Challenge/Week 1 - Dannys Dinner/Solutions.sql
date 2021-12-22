/* --------------------
   Case Study Questions
   --------------------

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
*/

#1.
Select S.customer_id, sum(M.price) from Sales S inner join Menu M on S.product_id=M.product_id group by 1

#2.
Select S.customer_id, count(distinct(S.order_date)) from Sales S  group by 1

#3
Select customer_id, product_id from 
(
Select S.customer_id,product_id, row_number() over(partition by customer_id order by order_date ) r1 from Sales S  ) tbl1 where r1=1

#4
Select product_id, count(product_id) cnt from sales group by 1 order by 2 desc limit 1

#5
Select customer_id, product_id from(
Select customer_id, product_id, cnt, row_number() over(partition by customer_id order by cnt desc) r1 from (Select customer_id, product_id, count(product_id) cnt from sales group by 1,2 order by 1,3 desc) tbl1) tbl2 where tbl2.r1=1

#6

Select Customer_id, Product_id from 
(Select S.Customer_id, S.order_Date, S.product_id, row_number() over( partition by customer_id order by order_date) r1 from Members M inner join Sales S 
on M.customer_id=S.customer_id 
where S.order_date>M.join_date) tbl1 where r1=1

#7
Select Customer_id, Product_id from 
(Select S.Customer_id, S.order_Date, S.product_id, rank() over( partition by customer_id order by order_date desc) r1 from Members M inner join Sales S 
on M.customer_id=S.customer_id 
where S.order_date<M.join_date) tbl1 where r1=1

#8
Select S.customer_id, sum(M.price) from Sales S inner join Menu M on S.product_id=M.product_id 
inner join Members Mem on Mem.Customer_id=S.Customer_id where S.order_date<Mem.join_date
group by 1;

#9

Select customer_id, sum(multiplier)
from(
Select customer_id, product_name, price, 
case when product_name = 'sushi' then (price*20)
	else (price*10)
    end as multiplier
from sales S inner join menu m on m.product_id=S.product_id) tbl1 group by 1

#10







