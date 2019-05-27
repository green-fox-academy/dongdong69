--Which product has the best average rating?

select products.name, avg(reviews.rating) as average_rating
from products, reviews
where products.id = reviews.product_id
group by products.name
order by average_rating DESC
limit 1;