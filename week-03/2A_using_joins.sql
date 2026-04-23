USE northwind;
-- 1. Find the cheapest item that Northwind sells
SELECT MIN(unitprice) AS CheapestPrice
FROM products;
-- pt 2 name of the cheapest item Northwind sells
SELECT productname, unitprice
FROM products
WHERE unitprice = (
    SELECT MIN(unitprice)
    FROM products
)