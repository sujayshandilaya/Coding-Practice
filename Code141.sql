select h.nationality, count(*) from airbnb_hosts h 
inner join airbnb_units u 
on h.host_id=u.host_id
where h.age<30 and u.unit_type='Apartment' group by 1 order by 2 desc

-----

select a.nationality, count(case when b.unit_type = 'Apartment' then 1 else null end) as apartment_count from airbnb_hosts a join airbnb_units b on a.host_id = b.host_id where a.age < 30 group by a.nationality 
having count(case when b.unit_type = 'Apartment' then 1 else null end) > 0
order by apartment_count desc