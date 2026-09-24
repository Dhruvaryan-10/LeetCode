With Ranked_emp AS (
    Select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        Dense_Rank() Over(
            Partition by e.departmentId
            order by e.salary desc
        ) as rnk
        from Employee e
        Left Join Department d
            ON e.departmentId = d.id
)
Select 
    Department,
    Employee,
    Salary 
From Ranked_emp 
Where rnk <=3;