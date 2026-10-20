CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, description, price, stock)
SELECT 'Demo T-shirt', 'A sample product for local development', 499.00, 25
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Demo T-shirt');

INSERT INTO products (name, description, price, stock)
SELECT 'Demo Backpack', 'A sample backpack product', 1299.00, 10
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Demo Backpack');
