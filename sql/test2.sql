SELECT
    strftime('%Y', `order`.order_received) AS "Year",
    COUNT(DISTINCT `order`.id) AS "Order count",
    COUNT(`order_line`.id) AS "Line count"
FROM
    `order`
INNER JOIN
    `order_line` ON `order`.id = `order_line`.order_id
WHERE
    strftime('%Y', `order`.order_received) BETWEEN '2010' AND '2020'
GROUP BY
    strftime('%Y', `order`.order_received)