
select dense_rank() over (order by n_messages desc), id_guest, n_messages from 
(
Select id_guest, sum(n_messages) as n_messages  from
airbnb_contacts group by 1
) tbl1;

-------

select dense_rank() over (order by sum(n_messages) desc), id_guest, sum(n_messages) from 
airbnb_contacts group by 2;

--Aggregate function can be applied on the elements inside the windows function. 