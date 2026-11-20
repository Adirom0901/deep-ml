-- your query
with t as (
SELECT *,DENSE_RANK() OVER(PARTITION BY region ORDER BY amount DESC )  AS DR FROM sales)

select DISTINCT region,amount from t 
where dr=1
order by region