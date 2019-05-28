--How can you produce a list of the start times for bookings by members named 'David Farrell'?
select starttime
from cd.bookings
join cd.members on cd.bookings.memid=cd.members.memid
where firstname='David' and
surname='Farrell';

--How can you produce a list of the start times for bookings for tennis courts, 
--for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
select starttime, name
from cd.bookings bok
join cd.facilities fac on bok.facid=fac.facid
where starttime between '2012-09-21' and '2012-09-22' and 
name like 'Tennis Court%';