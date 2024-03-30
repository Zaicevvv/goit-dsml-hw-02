--Отримати всі завдання певного користувача.
SELECT * FROM tasks WHERE user_id=1;
--Вибрати завдання за певним статусом.
SELECT *, s.name as status
FROM tasks AS t 
JOIN status AS s 
ON s.id = t.status_id 
WHERE user_id=1 
AND s.name='new';
--Оновити статус конкретного завдання.
update tasks set status_id=2
WHERE id=4
--Отримати список користувачів, які не мають жодного завдання.
select * from users where id not in(select user_id from tasks);
--Додати нове завдання для конкретного користувача.
insert into tasks(title, description, status_id, user_id) 
values('title', 'description', 1, 3);
--Отримати всі завдання, які ще не завершено.
select * from tasks where not status_id=3 
--Видалити конкретне завдання.
delete from tasks where id=1
--Знайти користувачів з певною електронною поштою.
select * from users where email like '%brian%'
--Оновити ім'я користувача.
update users set fullname='John Doe'
WHERE id=4 
--Отримати кількість завдань для кожного статусу.
SELECT COUNT(*), s.name
FROM tasks t
LEFT JOIN status s ON t.status_id = s.id
GROUP BY s.id;
--Отримати завдання, які призначені користувачам
--з певною доменною частиною електронної пошти.
SELECT *
FROM tasks
WHERE user_id IN (SELECT id
FROM users
where email like '%@example.com%');
--Отримати список завдань, що не мають опису.
select * from tasks where description=null
--Вибрати користувачів та їхні завдання,
--які є у статусі 'in progress'.
SELECT *
FROM users
JOIN tasks 
ON users.id = tasks.user_id 
WHERE status_id=2;
--Отримати користувачів та кількість їхніх завдань.
SELECT COUNT(*), u.fullname
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;