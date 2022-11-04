
Select round(sum(case when diff<=7 then 1 else 0 end)*100/count(user_id),2) as single_purchase_pct
from
(SELECT s.user_id, min((purchase_date::date-signup_date::date))as diff
FROM signups s
LEFT JOIN
user_purchases up
on s.user_id=up.user_id
group by 1)t1