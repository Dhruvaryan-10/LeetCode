# Write your MySQL query statement below
Select en.unique_id , e.name
from Employees e
left join EmployeeUNI en
on e.id = en.id;