
SELECT pp.profile_id FROM 
personal_profiles pp 
inner join
employee_company ec
on pp.profile_id=ec.personal_profile_id
inner join
company_pages cp
on cp.company_id=ec.company_id
group by pp.profile_id
having avg(pp.followers) > max(cp.followers)
order by pp.profile_id


##################

WITH popular_companies 
AS (
  SELECT
    employees.personal_profile_id,
	MAX(pages.followers) AS highest_followers
  FROM employee_company AS employees 
  LEFT JOIN company_pages AS pages
    ON employees.company_id = pages.company_id  
  GROUP BY employees.personal_profile_id)

SELECT profiles.profile_id
FROM popular_companies AS companies
LEFT JOIN personal_profiles AS profiles
	ON companies.personal_profile_id = profiles.profile_id
WHERE profiles.followers > companies.highest_followers
ORDER BY profiles.profile_id;