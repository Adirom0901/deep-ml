-- your query
WITH T AS (
SELECT customer_id,order_date,SUM(amount) as am FROM orders
WHERE order_date>='2024-01-01' AND order_date<='2024-01-31'
GROUP BY customer_id, order_date)

SELECT MAX(am) FROM T