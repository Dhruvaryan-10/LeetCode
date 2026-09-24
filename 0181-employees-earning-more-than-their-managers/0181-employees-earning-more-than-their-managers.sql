# Write your MySQL query statement below
Select 
    emp.name AS Employee
from Employee emp
JOIN Employee mgr
    ON emp.managerid = mgr.id
WHERE emp.salary > mgr.salary;