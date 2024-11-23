import psycopg2 as pg
from connect import create_connection




def execute_query(conn, sqlstring):
    try:
        c = conn.cursor()
        c.execute(sqlstring)
        results = c.fetchall()
        for row in results:
            print(row)
        conn.commit()
    except pg.Error as e:
        print(e)

if __name__ == '__main__':

    USER_ID = 1
    STATUS_ID = 1


    # SQL-запит для отримання всіх завдань певного користувача
    Q1 = f"""
    SELECT * FROM tasks WHERE user_id = {USER_ID};
    """
    #Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
    Q2 = f"""
    SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
    """

    #Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
    Q3 = f"""
    UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = {STATUS_ID};
    """

    #Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
    Q4 = f"""
    SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);
    """
    
    #Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
    Q5 = f"""
    INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task', 'New Task Description', 1, 1);
    """

    #Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
    Q6 = f"""
    SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
    """

    #Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
    Q7 = f"""
    DELETE FROM tasks WHERE id = 1;
    """

    #Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
    Q8 = f"""
    SELECT * FROM users WHERE email LIKE 'kim94@example.net';
    """

    #Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
    Q9 = f"""
    UPDATE users SET fullname = 'Rebecca Kim' WHERE id = 9;
    """

    #Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
    Q10 = f"""
    SELECT status.name, COUNT(tasks.id) FROM status LEFT JOIN tasks ON status.id = tasks.status_id GROUP BY status.name;
    """

    #Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
    Q11 = f"""
    SELECT * FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@example.net';
    """

    #Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
    Q12 = f"""
    SELECT * FROM tasks WHERE description IS NULL OR description = '';
    """

    #Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
    Q13 = f"""
    SELECT users.fullname, tasks.title FROM users INNER JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');
    """

    #Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
    Q14 = f"""
    SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname;
    """

    with create_connection() as conn:
        if conn is not None:
            print(">> Отримати всі завдання певного користувача:")
            execute_query(conn, Q1)
            print(">> Вибрати завдання за певним статусом:")
            execute_query(conn, Q2)
            print(">> Оновити статус конкретного завдання:")
            execute_query(conn, Q3)
            print(">> Отримати список користувачів, які не мають жодного завдання:")
            execute_query(conn, Q4)
            print(">> Додати нове завдання для конкретного користувача:")
            execute_query(conn, Q5)
            print(">> Отримати всі завдання, які ще не завершено:")
            execute_query(conn, Q6)
            print(">>Видалити конкретне завдання:")
            execute_query(conn, Q7)
            print(">> Знайти користувачів з певною електронною поштою:")
            execute_query(conn, Q8)
            print(">> Оновити ім'я користувача:")
            execute_query(conn, Q9)
            print(">> Отримати кількість завдань для кожного статусу:")
            execute_query(conn, Q10)
            print(">> Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти '@example.net':")
            execute_query(conn, Q11)
            print(">> Отримати список завдань, що не мають опису:")
            execute_query(conn, Q12)
            print(">> Вибрати користувачів та їхні завдання, які є у статусі 'in progress':")
            execute_query(conn, Q13)
            print(">> Отримати користувачів та кількість їхніх завдань:")
            execute_query(conn, Q14)

        else:
            print("Error! cannot create the database connection.")
