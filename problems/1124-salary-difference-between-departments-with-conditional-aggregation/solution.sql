WITH T AS (
    SELECT department,
           SUM(salary) OVER (
               PARTITION BY department
               ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
           ) AS tot_sum
    FROM (
        SELECT * FROM employees
        UNION ALL
        SELECT -1,'dummy', 'Engineering', 0
        UNION ALL
        SELECT -2,'dummy', 'Sales', 0
    ) t3
    WHERE department IN ('Engineering', 'Sales')
),
Eng AS (
    SELECT DISTINCT COALESCE(tot_sum, 0) AS eng_sum
    FROM T
    WHERE department = 'Engineering'
),
Sal AS (
    SELECT DISTINCT COALESCE(tot_sum, 0) AS sal_sum
    FROM T
    WHERE department = 'Sales'
)
SELECT eng_sum AS Engineering_total,
       sal_sum AS Sales_total,
       eng_sum - sal_sum AS salary_difference
FROM Eng CROSS JOIN Sal;
