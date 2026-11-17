-- your query
SELECT *,ROW_NUMBER() OVER(PARTITION BY department ORDER BY score DESC,employee) as rn
,RANK() OVER(PARTITION BY department ORDER BY score DESC) as rnk
, DENSE_RANK() OVER(PARTITION BY department ORDER BY score DESC) as dense_rnk 
FROM scores