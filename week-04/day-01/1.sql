--List the users who registered in 2018 with a .com email address and living in China

select *
from users
where extract(year from date_of_registration)=2018 and
email like '%.com%' and
country = 'China';