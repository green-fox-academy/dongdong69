--How many users registered in 2019?

select count(*) as number_users
from users
where extract(year from date_of_registration)=2019;