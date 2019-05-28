--Find the titles of all movies directed by Steven Spielberg. 
select title from movie
where director='Steven Spielberg';

--Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 

select year
from movie
where movie.mID in (select mID from Rating where stars=4 or stars=5)
order by year ASC;

--Find the titles of all movies that have no ratings. 
select title from movie where mID not in (select mID from rating);

--Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. 
select name from reviewer
join rating on reviewer.rid=rating.rid
where ratingdate is null;

--Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 

select name, title, stars, ratingdate from
(rating join reviewer on rating.rid=reviewer.rid) join movie on rating.mid=movie.mid
order by name, title, stars;