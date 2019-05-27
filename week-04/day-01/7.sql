--How many users left at least one field blank?

select count(*) number_blank
from users
where username is null or
gender is null or
email is null or
date_of_registration is null or
first_name is null or
last_name is null or
country is null;