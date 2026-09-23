# Write your MySQL query statement below
Select p.lastName, p.firstName , a.city, a.state
from Person p 
Left Join Address a
on p.personId = a.personId; 