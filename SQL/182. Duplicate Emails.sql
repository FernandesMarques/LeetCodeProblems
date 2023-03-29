-- https://leetcode.com/problems/duplicate-emails/
with base as (
    select email, count(email) as qt from Person P group by email
) select email from base where qt > 1