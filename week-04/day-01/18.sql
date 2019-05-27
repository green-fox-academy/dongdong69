--How many days passed since the last review?

select extract(day FROM (age(max(date) , now()))) days
from reviews;