--Which product has the worst rating?

select products.name, reviews.rating
from products, reviews
where products.id = reviews.product_id
order by reviews.rating ASC
limit 1;