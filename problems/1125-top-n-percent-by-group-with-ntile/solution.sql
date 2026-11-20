-- your query
with t as (
SELECT *,NTILE(4) OVER(PARTITION BY region ORDER BY amount DESC )  AS DR FROM sales)

select region,amount FROM T
WHERE dr=1
ORDER BY region