--What is the average price for an electric product?

select avg(price) as average_price
from products
where category='Electronics';