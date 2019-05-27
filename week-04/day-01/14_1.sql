--Which products have no review?

select * from products where products.id not in (select product_id from reviews);