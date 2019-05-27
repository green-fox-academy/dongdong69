--What is the gender ratio?

select sum(case when gender='Male' then 1 else 0 end) * 1.0 / sum(case when gender='Female' then 1 else 0 end)
from users;