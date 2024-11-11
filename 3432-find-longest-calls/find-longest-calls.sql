# Write your MySQL query statement below
with cte as(select first_name,c.contact_id, type,duration,
dense_rank() over(partition by type order by duration desc)as rn
from calls c
inner join contacts co
on co.id=c.contact_id)

select first_name,type,date_format(sec_to_time(duration), '%H:%i:%s') as duration_formatted
from cte
where type='incoming'
and rn between 1 and 3
union
select  first_name,type,date_format(sec_to_time(duration), '%H:%i:%s') as duration_formatted
from cte
where type='outgoing'
and rn between 1 and 3
order by 2 desc, 3 desc, 1 desc