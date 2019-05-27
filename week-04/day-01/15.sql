--How many reviews are 3 or below without comment?

select count(*) as number_reviews
from reviews
where rating <= 3 and 
comment is null;