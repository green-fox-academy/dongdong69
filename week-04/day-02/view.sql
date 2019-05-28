--Create a view where you display the reviewer's name and the amount of their review

create view amount_reviewer_review as
select name, count(*) as number_reviews
from reviewer
join rating on reviewer.rid=rating.rid
group by name;

--Create a view where you display the movies which have no review

create view movie_no_review as
select title
from movie
left join rating on movie.mid=rating.mid
where rating.mid is null;

--Create a view where you display all the directors (do not include null values)

create view movie_director as
select distinct director
from movie
where director is not null;

--Create a view where you display the movie title and the average rating

create view movie_rating as
select title, avg(stars) as average_rating
from movie
join rating on movie.mid=rating.mid
group by title;