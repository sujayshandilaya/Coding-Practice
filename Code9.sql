with
   stadium_groups as (
        select
        id, visit_date, people, (id- (rank() over (order by id))) as group_num
        from Stadium
        where people>=100 
    ),
    more_than_three as (
        select 
            group_num, count(group_num) as group_count
            from stadium_groups
            group by group_num
            having group_count>=3
    )
select 
id, visit_date, people
from stadium_groups g, more_than_three m
where g.group_num=m.group_num
order by visit_date;
