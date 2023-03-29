-- https://leetcode.com/problems/delete-duplicate-emails/
delete p from Person p, Person p2 
where p.email = p2. email and p.id > p2.id