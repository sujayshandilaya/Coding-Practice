SELECT employee_id, (365-sum((end_date-start_date))-count(ce.job_id)) as bench_days  from 
staffing s inner join consulting_engagements ce 
on s.job_id=ce.job_id
where s.is_consultant ='true'
group by employee_id;