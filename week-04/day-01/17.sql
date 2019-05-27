--List the average rating for each product

select product_id, avg(rating) as average_rating
from reviews
group by product_id
order by product_id ASC;