--Which products have no review?

select * from products
left join reviews
on products.id = reviews.product_id
where reviews.product_id is null;