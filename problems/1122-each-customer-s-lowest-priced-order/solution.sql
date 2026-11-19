-- your query
WITH T AS (
SELECT *,row_number() OVER(PARTITION BY customer_id order by amount,order_id) as mo  FROM orders)

SELECT order_id,customer_id,amount FROM T
WHERE mo=1
order by customer_id