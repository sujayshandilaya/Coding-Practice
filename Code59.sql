Select tbl1.date, cast(tbl1.cnt as decimal)/tbl2.tot_cnt
from
(select t1.date,count(*) as cnt from fb_friend_requests t1 
inner join
fb_friend_requests t2 on
t1.user_id_sender=t2.user_id_sender where t1.action='sent' and t2.action='accepted' group by 1 
) tbl1
inner join
(Select date, count(*) as tot_cnt from fb_friend_requests where action='sent' group by 1) tbl2

on tbl1.date=tbl2.date


--

Select tbl2.date, cast(count(tbl1.user_id_receiver) as decimal)/count(tbl2.user_id_sender)
from
(Select date, user_id_sender, user_id_receiver from fb_friend_requests where action='sent' ) tbl2
left join
(select t1.date,user_id_sender, user_id_receiver from fb_friend_requests t1 
 where t1.action='accepted' 
) tbl1
on tbl1.user_id_sender=tbl2.user_id_sender and tbl1.user_id_receiver=tbl2.user_id_receiver
group by 1