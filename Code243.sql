from
(SELECT date(measurement_time) as measurement_day, measurement_value, 
row_number() over(PARTITION BY date(measurement_time) order by measurement_time ) as rnum 
FROM measurements) t1
group by 1;