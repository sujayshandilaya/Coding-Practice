Select *, row_number() over (order by cnt desc,from_user) from
(select from_user, count(to_user) cnt from google_gmail_emails group by 1) tbl2