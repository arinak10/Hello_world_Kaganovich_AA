SELECT *
FROM products
WHERE category='электроника';

SELECT * 
FROM products
WHERE category='одежда' and name like '%женские%';

SELECT *
FROM products
WHERE NOT category = 'бытовая техника';

SELECT *
FROM products
where category='электроника' or category='одежда' or category='книги';

SELECT * 
FROM products
WHERE(category='электроника' and name like '%Samsung%') or category = 'бытовая техника';

SELECT * 
FROM products
WHERE((category='электроника' or category='одежда' or category='бытовая техника') and (id between 1 and 15) and not name like '%Samsung%') or category='книги';

