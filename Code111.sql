with tbl1 as
(Select user_id, paying_customer from ms_user_dimension u inner join ms_acc_dimension a on u.acc_id=a.acc_id)

Select date, non_paying, paying from
(
Select date, sum(case when paying_customer='no' then 1 else 0 end) as non_paying, sum(case when paying_customer='yes' then 1 else 0 end) as paying from ms_download_facts d inner join tbl1 t on d.user_id=t.user_id group by 1) t1
where non_paying > paying
order by date 

https://platform.stratascratch.com/coding/10300-premium-vs-freemium?python=