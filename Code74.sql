With tbl as (
Select date, sum(consumption) as total_energy
from
(
select * from fb_eu_energy
union all 
Select * from fb_asia_energy
union all
Select * from fb_na_energy
) tbl1 group by 1
)
Select date, total_energy 
from(
Select date, total_energy, rank() over (order by total_energy desc) as rnk from tbl
) tbl2 where rnk=1