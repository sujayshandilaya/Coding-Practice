Select c1.seat_id from Cinema c1 inner join Cinema c2 on c1.seat_id=c2.seat_id+1 or c1.seat_id=c2.seat_id-1 where c1.free=1 and c2.free=1 group by 1 order by 1


Select seat_id from
(
Select seat_id, free, lead(free,1) over(order by seat_id) as l1, lag(free,1) over(order by seat_id) as l2 from Cinema) t1 where free=1 and (l1=1 or l2=1) order by 1