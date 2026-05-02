SELECT * 
FROM prices
where price between 1000 and 50000;

SELECT * 
FROM prices
where (price between 500 and 70000) and id <= 5;

SELECT * 
FROM prices
where (price <100) or (price between 60000 and 70000);