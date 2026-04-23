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
);
-- 2. Average price of all products
SELECT AVG(UnitPrice) AS AveragePrice
FROM Products;
-- Bonus
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;
-- 3. Find the most expensive  thhat Northwind has
SELECT MAX(UnitPrice) AS HighestPrice
FROM Products;
-- pt 2 Find the name of the product with that price, plus the name of the supplier for that product.
SELECT p.ProductName, s.CompanyName AS SupplierName, p.UnitPrice
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
);
-- 4. The total sum of monthly payroll for employees.
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;
-- 5. List all employees salaries from highest to lowest. 
SELECT 
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;
-- 6. List the name, supplier ID of each supplier, and the number of items they supply.
SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName, s.SupplierID;
-- 7. List all categorty names and the average price for each category.
SELECT c.CategoryName, AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;
-- 8. List all suppliers that that provide at least 5 items and northwind and number of items they supply
SELECT s.CompanyName, COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;
-- 9. List inventory value by highest to lowest, multiply unitprice and number of inventory. If same amount list by product name. 
SELECT 
    ProductID,
    ProductName,
    (UnitPrice * UnitsInStock) AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;