--Which are the 3 most expensive products?

select name
from products
order by price DESC
limit 3;