-- your query
SELECT name,salary,title from workers w JOIN titles t ON w.title_id=t.title_id
WHERE salary= (SELECT MAX(salary) FROM workers)
ORDER BY name
