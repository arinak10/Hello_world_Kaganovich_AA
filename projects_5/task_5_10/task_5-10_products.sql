SELECT *
FROM products;

SELECT name, category
FROM products;

SELECT DISTINCT category
FROM products;

SELECT *
FROM products
ORDER BY name;

SELECT *
FROM products
ORDER BY name DESC;

SELECT *
FROM products
LIMIT 10;

SELECT *
FROM products
LIMIT 10 OFFSET 10;

SELECT *
FROM products
ORDER BY RANDOM()
LIMIT 5;

select category
FROM products
ORDER BY category asc;

SELECT *
FROM products
ORDER BY category, name;
