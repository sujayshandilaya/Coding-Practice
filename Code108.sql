select email from Person group by email having count(*)>1

--Subquery
select distinct email from Person a where exists (select 1 from person b where a.email=b.email)

--iner join

select distinct a.email from Person a 
inner join 
Person b
on a.email=b.email and a.id<>b.id