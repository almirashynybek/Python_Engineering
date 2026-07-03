1. Создайте таблицы students (id, name, gpa) и
courses (id, course_name, student_id).

CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	gpa NUMERIC(10,2) NOT NULL
)

CREATE TABLE courses(
	id SERIAL PRIMARY KEY,
	course_name VARCHAR(50) NOT NULL,
	student_id INTEGER NOT NULL,
	FOREIGN KEY (student_id) REFERENCES students(id)
)


2. Заполните таблицы данными

INSERT INTO students (name, gpa) 
VALUES ('Alice Brown', 3.85),
	('John Smith', 3.60),
	('Jane Doe', 3.92),
	('Bob White', 3.45),
	('Emma Green', 3.75);

INSERT INTO courses (course_name, student_id) 
VALUES 
	('Mathematics', 1), -- Alice Brown
	('Mathematics', 2), -- John Smith
	('Mathematics', 3), -- Jane Doe
	('Physics', 4),     -- Bob White
	('Biology', 5),     -- Emma Green
	('History', 1),     -- Alice Brown
	('Computer Science', 2), -- John Smith
	('Philosophy', 3),  -- Jane Doe
	('Economics', 4),   -- Bob White
	('Mathematics', 5); -- Emma Green


3. Напишите запрос с множественным подзапросом, который выведет всех студентов,
чей средний балл выше среднего балла по курсу "Mathematics".

SELECT *          --first method
FROM students
WHERE gpa > (
    SELECT AVG(gpa)
    FROM students
    WHERE id IN (
        SELECT student_id
        FROM courses
        WHERE course_name = 'Mathematics'
    )
)

SELECT s.name AS student_name        --second method 
FROM students s 
WHERE gpa > (
	SELECT AVG(st.gpa) 
	FROM students st
	JOIN courses c ON st.id = c.student_id
	WHERE c.course_name = 'Mathematics'
)

4. Напишите запрос с коррелированным подзапросом, который выведет студентов, 
чей балл выше среднего балла по их курсу.

SELECT DISTINCT s.name AS student_name, s.gpa, c.course_name 
FROM students s
JOIN courses c ON s.id = c.student_id
WHERE s.gpa > (
	SELECT AVG(st.gpa)
	FROM students st 
	JOIN courses co ON st.id = co.student_id
	WHERE co.course_name = c.course_name
)






1. Создайте таблицы departments (id, name, budget) и 
employees (id, name, department_id, salary).

CREATE TABLE departments(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	budget NUMERIC(10,2) NOT NULL
)

CREATE TABLE employees(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	department_id INTEGER NOT NULL,
	salary NUMERIC(10,2) NOT NULL,
	FOREIGN KEY (department_id) REFERENCES departments(id)
)


2. Заполните таблицы данными

INSERT INTO departments (name, budget) 
VALUES
	('Human Resources', 500000.00),
	('Engineering', 2000000.00),
	('Marketing', 800000.00),
	('Sales', 1500000.00),
	('IT Support', 600000.00);

INSERT INTO employees (name, department_id, salary) 
VALUES
	('Alice Brown', 1, 65000.00), -- Human Resources
	('John Smith', 2, 120000.00), -- Engineering
	('Jane Doe', 2, 130000.00),   -- Engineering
	('Bob White', 3, 75000.00),   -- Marketing
	('Emma Green', 4, 90000.00),  -- Sales
	('Liam Black', 4, 95000.00),  -- Sales
	('Sophia Blue', 5, 70000.00), -- IT Support
	('Ethan Grey', 5, 72000.00);  -- IT Support

SELECT * FROM departments

3. Напишите запрос с скалярным подзапросом,
который найдет отдел с максимальным бюджетом.

SELECT name 
FROM departments
WHERE budget = (
	SELECT MAX(budget) FROM departments)


4. Используя коррелированный подзапрос, найдите
сотрудников, чья зарплата выше средней по отделу.

SELECT DISTINCT e.name AS employee_name, e.salary, d.name AS department_name
FROM employees e
JOIN departments d ON d.id = e.department_id
WHERE e.salary > (
    SELECT AVG(em.salary)
    FROM employees em
    WHERE em.department_id = e.department_id
);