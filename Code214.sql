
Select round(sum(tiv_2016),2) as tiv_2016  from(Select tiv_2016, count(*) over(partition by tiv_2015) cnt1, count(*) over(partition by lat,lon) cnt2 from Insurance)tbl1 where cnt1>1 and cnt2=1