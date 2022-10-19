SELECT pp.profile_id FROM 
personal_profiles pp 
inner join
company_pages cp
on cp.company_id=pp.employer_id
where pp.followers>cp.followers
order by pp.profile_id;