-- your query
SELECT * FROM employees e1 
WHERE e1.salary > (SELECT avg(salary) FROM employees e2 WHERE e2.department =e1.department)
ORDER BY id 
