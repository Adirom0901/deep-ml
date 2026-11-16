-- your query
WITH T AS(
SELECT *, MIN(id) OVER(PARTITION BY email) as mind FROM person)

SELECT id,email 
FROM t
WHERE id=mind
ORDER BY id