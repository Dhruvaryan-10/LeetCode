# Write your MySQL query statement below
SELECT class
from Courses 
GROUP by class
HAVING COUNT(*) >= 5;