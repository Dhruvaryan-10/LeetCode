# Write your MySQL query statement below
Select mgr.name 
from Employee emp
Join Employee mgr
on emp.managerId = mgr.id
group by mgr.id,mgr.name
having count(*) >= 5;