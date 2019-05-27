--How many users registered in January?

select count(*) as number_users
from users
where extract(month from date_of_registration)=1;