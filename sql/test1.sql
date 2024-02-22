SELECT
    user.id AS "User ID",
    user.first_name || ' ' || user.last_name AS "Full name",
    `order`.id AS "Order ID",
    CASE
        WHEN `order`.order_delivered IS NOT NULL THEN 'Delivered'
        WHEN `order`.order_shipped IS NOT NULL THEN 'Shipped'
        WHEN `order`.order_prepared IS NOT NULL THEN 'Prepared'
        WHEN `order`.payment_received IS NOT NULL THEN 'Paid'
        WHEN `order`.order_received IS NOT NULL THEN 'Received'
    END AS "Order Status"
FROM
    user
INNER JOIN
    `order` ON user.id = `order`.user_id
WHERE
    `order`.id BETWEEN 1337 AND 1500
ORDER BY
    user.last_name DESC;
