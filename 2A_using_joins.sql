USE northwind;
-- 1. List all products by  product id, product name, unit price and category name. Order by category name
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;
-- 2. List all products that cost more then $75 order by product name
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;
-- 3. List product, catergory, and supplier, order by product name
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;
-- 4. List every order shipped to Germany and shipper name.
SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    sh.CompanyName AS Shipper
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY sh.CompanyName, o.ShipName;
-- 5. Keep #4 remove orderid, group by shipname, and add count of orders per shipname 
SELECT 
    o.ShipName,
    sh.CompanyName AS Shipper,
    COUNT(*) AS TotalOrders
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
GROUP BY o.ShipName, sh.CompanyName
ORDER BY sh.CompanyName, o.ShipName;
-- 6. All orders that included the product “Sasquatch Ale"
SELECT 
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM Orders o
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';
