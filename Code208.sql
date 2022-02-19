# write your mysql query statement belowSELECT username,
       activity,
       startdate,
       enddate
FROM   (
                SELECT   *,
                         Row_number() OVER(partition BY username ORDER BY startdate DESC) rnum,
                         Count(*) OVER(partition BY username)                             cnt
                FROM     useractivity)tbl1
WHERE  rnum =2
OR     cnt=1