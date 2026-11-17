-- your query
SELECT DISTINCT l.num as num from logs l JOIN logs l2 ON l.id=l2.id-1 AND l.num =l2.num JOIN 
logs l3 ON l.id=l3.id-2 AND  l.num=l3.num 
order by num