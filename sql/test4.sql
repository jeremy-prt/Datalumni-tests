WITH UserRanks AS (
    SELECT
        user.id AS "User ID",
        user.first_name || ' ' || user.last_name AS "Full name",
        RANK() OVER (ORDER BY SUM(order_line.unit_price) DESC) AS "Rank 2018"
    FROM
        user
    INNER JOIN
        `order` ON user.id = `order`.user_id
    INNER JOIN
        order_line ON `order`.id = order_line.order_id
    WHERE
        strftime('%Y', `order`.order_received) = '2018'
    GROUP BY
        user.id
    ORDER BY
        "Rank 2018"
    LIMIT 10
)

SELECT
    UserRanks."User ID",
    UserRanks."Full name",
    UserRanks."Rank 2018",
    RANK() OVER (ORDER BY SUM(order_line.unit_price) DESC) AS "Rank 2019"
FROM
    UserRanks
INNER JOIN
    `order` ON UserRanks."User ID" = `order`.user_id
INNER JOIN
    order_line ON `order`.id = order_line.order_id
WHERE
    strftime('%Y', `order`.order_received) = '2019'
GROUP BY
    UserRanks."User ID"
ORDER BY
    "Rank 2018";
