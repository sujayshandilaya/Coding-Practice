Select count(*) from
(
Select row_number() over(PARTITION BY company_id,title, description order by job_id) as rnum 
from job_listings )t1 where rnum>1

######################

Select count(*) from 
(
Select count(*) as cnt from job_listings group by company_id,title, description having
count(*)>1
)t1