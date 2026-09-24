# Write your MySQL query statement below
Select w.id 
from weather w
Join weather wth
on DATEDIFF(w.recordDate, wth.recordDate) = 1
where w.temperature > wth.temperature;