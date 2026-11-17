-- your query
SELECT w1.recorded_on as curr FROM weather w1 JOIN weather w2 ON  w1.recorded_on-W2.recorded_on=1 and w1.temperature >w2.temperature
ORDER BY w1.recorded_on 