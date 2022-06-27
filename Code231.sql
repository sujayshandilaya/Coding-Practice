with cte as (Select department_id, date_format(pay_date,'%Y-%m') as month , avg(amount) as avg_dept from Salary S inner join Employee E on S.employee_id=E.employee_id group by 1,2),

cte1 as (Select date_format(pay_date,'%Y-%m') as month , avg(amount) as avg_company from Salary group by 1)

Select cte.month as pay_month, department_id, case when avg_dept>avg_company then 'higher' when avg_dept<avg_company then 'lower' else 'same' end as comparison from cte inner join cte1 using(month)