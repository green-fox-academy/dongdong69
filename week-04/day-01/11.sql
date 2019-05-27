--How much would it cost me to buy all the toys?

select sum(price) as all_price
from products
where category='Toys';