# Write your MySQL query statement below
with

requester_count as (
    select
        requester_id as id,
        count(*) as num
    from RequestAccepted
    group by 1
),

accepter_count as (
    select
        accepter_id as id,
        count(*) as num
    from RequestAccepted
    group by 1
),

total_count as (
    select
        id,
        sum(num) num
    from (
        select id, num
        from requester_count rc
        union all
        select id, num
        from accepter_count ac
    ) rac
    group by 1
)

select *
from total_count
order by num desc
limit 1