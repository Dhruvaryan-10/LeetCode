# Write your MySQL query statement below
Select 
    d.name AS Department ,
    e.name AS Employee,
    e.salary
from Employee e
Left Join Department d
    on e.departmentId = d.id
Where (e.departmentId, e.salary) in (
    Select departmentId , MAX(salary)
    from Employee
    Group BY departmentId
)
