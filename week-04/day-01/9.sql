--Which are the 4th and 5th cheapest products?

select name
from products
order by price ASC
limit 2 offset 3;