-- Задание 1: Работа с заказами

-- CREATE TABLE online_orders (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_name VARCHAR(50) NOT NULL,
-- 	order_date DATE NOT NULL,
-- 	amount NUMERIC(10, 2) NOT NULL
-- )

-- INSERT INTO online_orders (customer_name, order_date,amount)
-- VALUES
-- 	('Alice', '2024-01-10', 500.00),
-- 	('Bob', '2024-01-15', 700.00),
-- 	('Charlie', '2024-01-20', 300.00)


-- CREATE TABLE offline_orders (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_name VARCHAR(50) NOT NULL,
-- 	order_date DATE NOT NULL,
-- 	amount NUMERIC(10, 2) NOT NULL
-- )

-- INSERT INTO offline_orders (customer_name, order_date, amount)
-- VALUES
-- 	('Diana', '2024-01-12', 400.00),
-- 	('Eve', '2024-01-18', 600.00),
-- 	('Frank', '2024-01-22', 200.00)



-- 3.Напишите запрос с UNION, который объединит заказы из обеих
-- таблиц, добавив колонку order_type (Online/Offline).

-- SELECT customer_name, order_date, amount, 'Online' AS order_type
-- FROM online_orders
-- UNION
-- SELECT customer_name, order_date, amount, 'Offline' AS order_type
-- FROM offline_orders


-- 4.Напишите запрос с UNION ALL, чтобы вывести заказы клиентов, 
-- чья сумма превышает 500, включая дублирующиеся записи.

-- SELECT customer_name, amount
-- FROM online_orders
-- WHERE amount > 500
-- UNION ALL
-- SELECT customer_name, amount
-- FROM offline_orders
-- WHERE amount > 500






-- Задание 2: Работа с подписчиками

-- CREATE TABLE email_subscribers (
-- 	id SERIAL PRIMARY KEY,
-- 	subscriber_name VARCHAR(50) NOT NULL,
-- 	subscription_date DATE NOT NULL
-- )

-- INSERT INTO email_subscribers (id, subscriber_name, subscription_date) 
-- VALUES
-- 	(1, 'Alice Johnson', '2024-01-15'),
-- 	(2, 'Bob Smith', '2024-01-20'),
-- 	(3, 'Charlie Brown', '2024-01-25'),
-- 	(4, 'Diana Prince', '2024-02-01')


-- CREATE TABLE sms_subscribers (
-- 	id SERIAL PRIMARY KEY,
-- 	subscriber_name VARCHAR(50) NOT NULL,
-- 	subscription_date DATE NOT NULL
-- )

-- INSERT INTO sms_subscribers (id, subscriber_name, subscription_date) 
-- VALUES
-- 	(1, 'Alice Johnson', '2024-01-18'),
-- 	(2, 'Eve Adams', '2024-01-22'),
-- 	(3, 'Frank Wilson', '2024-01-28'),
-- 	(4, 'Charlie Brown', '2024-02-05')

-- 3.Напишите запрос с UNION, чтобы объединить списки подписчиков
-- электронной почты и SMS с сортировкой по дате подписки.

-- SELECT subscriber_name, subscription_date 
-- FROM email_subscribers
-- UNION
-- SELECT subscriber_name, subscription_date 
-- FROM sms_subscribers
-- ORDER BY subscription_date ASC


-- 4.Используя UNION, найдите уникальные даты
-- подписки и отсортируйте их по возрастанию.

-- SELECT subscription_date FROM email_subscribers
-- UNION
-- SELECT subscription_date FROM sms_subscribers
-- ORDER BY subscription_date ASC