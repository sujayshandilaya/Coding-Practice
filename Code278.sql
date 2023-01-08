# Write your MySQL query statement below
Select distinct id, name from
(
Select l.id, a.name, login_date, lag(login_date,4) over(partition by id order by login_date) as l1,
date_sub(login_date,interval 4 day) as diff
 from
 (Select distinct id, login_date from logins )l
 inner join
 Accounts a on
 l.id=a.id)t1
 where l1=diff order by id