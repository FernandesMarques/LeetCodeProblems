-- https://leetcode.com/problems/customers-who-never-order
select name as Customers from Customers c
where c.id not in (select customerId from Orders)