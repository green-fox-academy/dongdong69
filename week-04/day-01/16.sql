--Which user reviewed the most?

select users.username, count(*) as most_reviewed_user
from users, reviews
where users.id=reviews.user_id
group by users.username
order by most_reviewed_user DESC
limit 1;