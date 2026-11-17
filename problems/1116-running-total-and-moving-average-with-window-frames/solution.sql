-- your query
SELECT *, SUM(amount) OVER(ORDER BY day) as running_total, AVG(amount) OVER(ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg  FROM  sales
