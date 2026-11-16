-- your query
WITH T AS (
SELECT salary, DENSE_RANK() OVER(order by salary DESC) as dr from employee)

SELECT distinct salary from t 
WHERE dr=3
