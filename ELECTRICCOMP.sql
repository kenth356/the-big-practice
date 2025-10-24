CREATE DATABASE IF NOT EXISTS electric_company;

USE electric_company;

SET sql_safe_updates = OFF;

CREATE TABLE IF NOT EXISTS customers(
customer_id INT PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(50),
meter_id INT,
classification VARCHAR(50),
total_kw_usage DECIMAL(10, 2),
rate_per_kw_usage DECIMAL(10, 2),
gross_amt DECIMAL(10, 2),
misce_charges DECIMAL(10, 2),
total_amount DECIMAL(10, 2),
previous_reading DECIMAL(10, 2),
current_reading DECIMAL(10, 2)
);

SELECT * FROM customers;