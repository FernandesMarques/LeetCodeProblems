-- https://leetcode.com/problems/employees-earning-more-than-their-managers
--#1 without join
select a.name as Employee 
from Employee a 
where e.salary > (select salary from Employee where id=a.managerId)

--#2 with join 
SELECT b.name as Employee
FROM employee a
INNER JOIN employee b ON a.id = b.managerID
WHERE
a.salary < b.salary