# Write your MySQL query statement below
Select p.product_id, p.product_name
from Product p
left join Sales s
on p.product_id = s.product_id
group by p.product_id,p.product_name
having MIN(s.sale_date) >= '2019-01-01'
and MAX(s.sale_date) <= '2019-03-31';