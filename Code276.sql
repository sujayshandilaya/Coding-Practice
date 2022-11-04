
Select sale_date, sum(case when fruit='apples' then sold_num else -1*sold_num end) as diff
from Sales
group by 1 order by 1