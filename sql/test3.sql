SELECT
    `order`.user_id AS "Missing user ID"
FROM
    `order`
LEFT JOIN
    user ON `order`.user_id = user.id
WHERE
    user.id IS NULL;
