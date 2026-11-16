
WITH T AS (
    SELECT
        EXTRACT(YEAR FROM sale_date) AS y,
        EXTRACT(MONTH FROM sale_date) AS mth,
        amount
    FROM sales
),
T1 AS (
    SELECT
        y,
        mth,
        SUM(amount) AS revenue
    FROM T
    GROUP BY y, mth
),
T2 AS (
    SELECT
        y,
        mth,
        revenue,
        LAG(revenue) OVER (ORDER BY y, mth) AS prev_rev
    FROM T1
)

SELECT
    MAKE_DATE(y::int, mth::int, 1)::TIMESTAMP AS month,
    revenue,
    ROUND(
        (revenue - prev_rev) * 100.0 / NULLIF(prev_rev, 0),
        2
    ) AS pct_change
FROM T2
ORDER BY y, mth;
