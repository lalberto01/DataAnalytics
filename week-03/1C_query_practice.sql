USE northwind;
-- 1. List product id, product name, and unit price in ascending order by price
SELECT ProductId, ProductName, UnitPrice
FROM products
ORDER BY unitprice ASC;
-- 2. List products that are at least 100 in hand by price descending 
SELECT ProductId, ProductName, UnitPrice
FROM products
WHERE unitsinstock >= 100
ORDER BY unitprice DESC
-- 3. List products that are at least 100 in hand by price descending and if prices are same, sort by product name( A to Z)
SELECT Productid, ProductName, UnitPrice
FROM products
WHERE unitsinstock >= 100
ORDER BY unitprice DESC, productname ASC;
-- 4. The total number of distinct customers who have placed orders,
SELECT COUNT(DISTINCT customerid) AS CustomerCount
FROM orders;
-- 5. Distinct customers per country where orders were shipped
SELECT shipcountry, COUNT(DISTINCT customerid) AS CustomerCount
FROM orders
GROUP BY shipcountry
ORDER BY CustomerCount DESC;
-- 6. Products with less than 25 on hand but on order
SELECT productid, productname, unitsinstock, unitsonorder
FROM products
WHERE unitsinstock < 25
AND unitsonorder >= 1
ORDER BY unitsonorder DESC, productname ASC;
-- 7. List employees per job title
SELECT title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY title;
-- 8. List employees with salary between 2000 and 2500, ordered by job title
SELECT employeeid, firstname, lastname, title, salary
FROM employees
WHERE salary BETWEEN 2000 AND 2500
ORDER BY title;
