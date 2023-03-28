-- https://leetcode.com/problems/nth-highest-salary/description/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 set N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select  distinct Salary
      from Employee order by Salary desc limit 1 OFFSET N 
  );
END