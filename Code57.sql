 Select 
 case when month <=9 then concat(year,'-','0',month)
 else concat(year,'-',month) end, 
 round(((val-prev_val)/prev_val)*100,2) from
 (
select extract(year from created_at) as year, extract(month from created_at) as month, sum(value) as val, lag(sum(value),1) over( order by extract(year from created_at), extract(month from created_at) ) as prev_val  from sf_transactions group by 1,2) tbl1