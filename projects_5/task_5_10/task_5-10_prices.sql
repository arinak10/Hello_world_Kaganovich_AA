SELECT *
FROM prices
ORDER BY price DESC
LIMIT 5;

SELECT *
FROM prices
ORDER BY created_at DESC
LIMIT 10;

SELECT *
FROM prices
ORDER BY price
LIMIT 10;

SELECT *
FROM prices
ORDER BY price DESC
offset 20;
