# Write your MySQL query statement below
with recursive month as (
    select 1 as month
    union
    select month + 1 as month from month where month < 10
)

, month_rides as(
    select   
        MONTH(r.requested_at) as month,
        sum(a.ride_distance) as ride_distance,
        sum(a.ride_duration) as ride_duration
    from Rides r 
    join AcceptedRides a on a.ride_id = r.ride_id
    where YEAR(r.requested_at) = '2020'
    group by month
)

select 
    m.month,
    ifnull(round(sum(mr.ride_distance)/3,2),0) as average_ride_distance,
    ifnull(round(sum(mr.ride_duration)/3,2),0) as average_ride_duration
from month m
left join month_rides mr
on ((mr.month - m.month = 0) 
    or (mr.month - m.month = 1)
    or (mr.month - m.month = 2))
group by 1
order by 1