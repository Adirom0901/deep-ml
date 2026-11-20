-- your query
WITH T AS (
SELECT user_id,login_date, DENSE_RANK() over(PARTITION BY user_id ORDER BY login_date) As dr FROM logins 
WHERE user_id IN (
SELECT DISTINCT l1.user_id FROM logins l1 JOIN logins l2 ON l1.user_id=l2.user_id AND l2.login_date-l1.login_date=1)
)

SELECT user_id, login_date as first_login FROM t
WHERE dr=1
ORDER BY user_id