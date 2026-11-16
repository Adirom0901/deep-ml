-- your query
WITH T AS (
SELECT *, DENSE_RANK() OVER( PARTITION BY department ORDER BY salary desc) as dr
FROM employees 
)

SELECT department,name,salary,dr FROM T WHERE dr<4 
ORDER BY department,salary desc,name