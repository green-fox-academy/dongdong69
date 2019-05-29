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

--How can you output a list of all members who have recommended another member? 
--Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).
select firstname, surname
from cd.members
where memid in (select recommendedby from cd.members)
order by surname, firstname;

--How can you output a list of all members, including the individual who recommended them (if any)? 
--Ensure that results are ordered by (surname, firstname).
select mem2.firstname as memfname, mem2.surname as memsname, mem1.firstname, mem1.surname
from cd.members mem1
right join cd.members mem2 on mem1.memid=mem2.recommendedby
order by mem2.surname, mem2.firstname;

--How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, 
--and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name.
select distinct concat(firstname, ' ', surname) as member, name
from (cd.bookings bok join cd.members mem on bok.memid=mem.memid)
join cd.facilities fac on bok.facid=fac.facid
where name like 'Tennis Court%'
order by member;

--How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'),
--and the guest user is always ID 0. Include in your output the name of the facility, 
--the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.
select concat(firstname, ' ', surname) as member, name, 
case when bok.memid=0 then bok.slots * guestcost
else bok.slots * membercost
end as cost
from (cd.bookings bok join cd.members mem on bok.memid=mem.memid)
join cd.facilities fac on bok.facid=fac.facid
where bok.starttime between '2012=09-14'and '2012=09-15' and
((mem.memid = 0 and bok.slots*fac.guestcost > 30) or
 (mem.memid != 0 and bok.slots*fac.membercost > 30))
order by cost DESC;

--How can you output a list of all members, including the individual who recommended them (if any), without using any joins? 
--Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.
select distinct concat(mem.firstname, ' ', mem.surname) as member,
(select concat(re.firstname, ' ', re.surname) as recommender
 from cd.members re
 where re.memid=mem.recommendedby)
 from cd.members mem
 order by member;