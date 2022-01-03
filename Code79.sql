
select tbl1.type, cast(cnt_processed as decimal)/cnt
from
(select type, count(*) as cnt_processed from facebook_complaints where processed = True  group by 1,processed) tbl1 inner join (Select type, count(*) as cnt from facebook_complaints group by type) tbl2
on tbl1.type=tbl2.type
--------

Select type, avg(case when processed then 1 else 0 end) from facebook_complaints group by 1