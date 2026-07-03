-- Задание 2: Работа с командами и менеджерами

-- CREATE TABLE managers(
-- 	id SERIAL PRIMARY KEY,
-- 	manager_name VARCHAR(50) NOT NULL,
-- 	department VARCHAR(50) NOT NULL
-- )

-- CREATE TABLE teams(
-- 	id SERIAL PRIMARY KEY,
-- 	team_name VARCHAR(50) NOT NULL,
-- 	manager_id INTEGER,
-- 	FOREIGN KEY (manager_id) REFERENCES managers(id)
-- )

-- INSERT INTO managers (id, manager_name, department) 
-- VALUES
-- 	(1, 'Alice Johnson', 'Engineering'),
-- 	(2, 'Bob Smith', 'Marketing'),
-- 	(3, 'Charlie Brown', 'Human Resources'),
-- 	(4, 'Diana Prince', 'Finance');

-- INSERT INTO teams (id, team_name, manager_id) 
-- VALUES
-- 	(1, 'Developers', 1),
-- 	(2, 'Marketers', 2),
-- 	(3, 'Recruiters', 3),
-- 	(4, 'Analysts', 4),
-- 	(5, 'QA Engineers', 1),
-- 	(6, 'Social Media Team', 2);


-- 3. Напишите запрос с использованием LEFT JOIN, чтобы найти все 
-- команды и их менеджеров, включая команды без менеджеров.

-- SELECT m.manager_name AS manager_name, t.team_name AS team_name
-- FROM managers m
-- LEFT JOIN  teams t ON m.id = t.manager_id


-- 4. Используя SELF JOIN, составьте иерархию
-- менеджеров, показывая, кто кому подчиняется.

-- ALTER TABLE managers
-- ADD COLUMN supervisor_id INT NULL; -- Может быть NULL для топ-менеджера


-- UPDATE managers
-- SET supervisor_id = NULL -- Топ-менеджер
-- WHERE id = 1; -- Alice Johnson

-- UPDATE managers
-- SET supervisor_id = 1
-- WHERE id IN (2, 3); -- Bob Smith и Charlie Brown подчиняют Alice

-- UPDATE managers
-- SET supervisor_id = 2
-- WHERE id = 4; -- Diana Prince подчиняется Bob


-- SELECT 
--     m1.manager_name AS manager,
--     m2.manager_name AS supervisor
-- FROM 
--     managers m1
-- LEFT JOIN 
--     managers m2 ON m1.supervisor_id = m2.id;
