-- CREATE TABLE employees (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL,
-- 	position VARCHAR(50),
-- 	salary NUMERIC(10, 2),
-- 	hire_date DATE DEFAULT CURRENT_DATE
-- )

-- добавили новый столбец называемый department
-- ALTER TABLE employees ADD COLUMN department VARCHAR(50) 

-- INSERT INTO employees (name, position, salary, hire_date, department) 
-- VALUES ('John', 'Developer', 55000.00,'2023-01-15', 'IT'),
-- ('Jane', 'Manager', 75000.00, '2022-06-01', 'Sales'),
-- ('Sam', 'Intern', 60000.00, '2023-12-10','Marketing'),
-- ('Smith', 'Analytic', 70000.00, '2023-06-15', 'IT'),
-- ('Brown', 'Intern', 50000.00, '2024-09-19','Sales')


-- Задание 1: Операции с данными (SELECT, INSERT, UPDATE, DELETE)

-- 1. Добавление данных: Michael Scott
-- INSERT INTO employees (name, position, salary, hire_date, department) 
-- VALUES('Michael Scott', 'Regional Manager', 75000, '2022-05-01,','Sales')


-- 2. Обновление данных:
-- UPDATE employees 
-- SET salary = salary + (salary*0.1) 
-- WHERE department = 'IT'


-- 3. Удаление данных:
-- DELETE FROM employees WHERE position = 'Intern'


-- 4. Вывод данных:
-- SELECT name, position 
-- FROM employees 
-- WHERE hire_date > '2020-01-01' ORDER BY hire_date DESC




-- Задание 2: Фильтрация строк (WHERE, LIKE, AND, OR)

-- INSERT INTO employees (name, position, salary, hire_date, department) 
-- VALUES ('Jason', 'IOS Developer', 55000.00,'2023-01-15', 'IT'),
-- ('Daniel', 'Manager', 75000.00, '2024-06-01', 'Finance'),
-- ('Steven', 'Intern', 60000.00, '2023-12-10','Marketing'),
-- ('Anderson', 'Analytic', 70000.00, '2023-06-15', 'IT'),
-- ('Anthony', 'Intern', 50000.00, '2024-09-19','Sales')


-- 1. Фильтрация с числовым условием:
-- SELECT name 
-- FROM employees 
-- WHERE (salary BETWEEN 50000 AND 80000) AND (department = 'IT' OR department = 'Finance')


-- 2. Использование LIKE:
-- SELECT name 
-- FROM employees 
-- WHERE name LIKE 'A%' OR name LIKE '%son%'


-- 3. Сложные условия:

-- INSERT INTO employees (name, position, salary, hire_date, department) 
-- VALUES ('Paul', 'Content creater', 80000.00,'2021-06-13', 'Marketing'),
-- ('Brian', 'Manager', 50000.00, '2022-06-01', 'Marketing'),
-- ('George', 'Intern', 65000.00, '2024-12-10','Marketing')

-- SELECT name 
-- FROM employees 
-- WHERE salary > 40000 AND hire_date < '2023-01-01' AND department='Marketing'




-- Задание 3: Сортировка, агрегирующие функции и группировка (ORDER
-- BY, COUNT, AVG, GROUP BY)

-- 1. Сортировка:
-- SELECT * 
-- FROM employees
-- ORDER BY department ASC, salary DESC;


-- 2. Агрегирующие функции:
-- SELECT 
--     MIN(salary) AS min_salary,
--     MAX(salary) AS max_salary,
--     AVG(salary) AS avg_salary
-- FROM employees


-- 3. Группировка с фильтрацией:
-- SELECT department, COUNT(*) AS employee_count
-- FROM employees
-- GROUP BY department
-- HAVING COUNT(*) >= 3;


-- 4. Дополнительно:
-- SELECT position, AVG(salary) AS avg_salary
-- FROM employees
-- GROUP BY position 
-- HAVING AVG(salary) > 60000
	
	