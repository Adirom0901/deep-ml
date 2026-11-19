-- your query
WITH T AS (
SELECT company, SUM(profit) as p from sales
GROUP BY company )
,T1 AS (
SELECT *,dense_rank() OVER(order by p desc) as dr FROM t)

SELECT company,p as total_profit FROM t1 
WHERE dr<=3
order by total_profit desc,company
