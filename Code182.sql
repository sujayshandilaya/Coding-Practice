Select rating, min(price), avg(price), max(price)
from
(
select concat(price, room_type, host_since, zipcode,number_of_reviews), price,
case when number_of_reviews > 40 then 'Hot'
when number_of_reviews >= 16 then 'Popular'
when number_of_reviews >=6 then 'Trending Up'
when number_of_reviews >=1 then 'Rising'
when number_of_reviews = 0 then 'New'
end as rating
from airbnb_host_searches group by 1,2,number_of_reviews ) tbl group by 1;