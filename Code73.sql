with tbl1 as (
Select users, count(users) as cnt from
(
Select user1 as users from facebook_friends 
union all 
select user2 as users from facebook_friends
)tbl 
group by users order by users
)

Select users, (cast(cnt as decimal)/ (Select count(users) from tbl1))*100 from tbl1