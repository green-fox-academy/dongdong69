--Which country has the most users?

select country, count(*) as number_users
from users
group by country
order by number_users DESC
limit 1;