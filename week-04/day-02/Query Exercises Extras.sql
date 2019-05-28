--Find the names of all reviewers who rated Gone with the Wind.

select distinct name from
(rating join reviewer on rating.rid=reviewer.rid) join movie on rating.mid=movie.mid
where title='Gone with the Wind';

--For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. 
select distinct name,title,stars from
(rating join reviewer on rating.rid=reviewer.rid) join movie on rating.mid=movie.mid
where director=name;