-- your query
SELECT e1.name FROM employees e1 JOIN employees e2 ON e1.manager_id= e2.id
WHERE e1.salary>e2.salary
