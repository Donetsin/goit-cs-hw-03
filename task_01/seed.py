from connect import create_connection

from faker import Faker
import random

# Підключення до бази даних
with create_connection() as conn:
    cur = conn.cursor()

    # Ініціалізація Faker
    fake = Faker()

    # Вставка фіксованих значень у таблицю status
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", (status,))

    # Вставка випадкових значень у таблицю users
    for _ in range(10):  # Вставляємо 10 випадкових користувачів
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (fullname, email))

    # Отримання всіх ID з таблиць status та users
    cur.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cur.fetchall()]

    # Вставка випадкових значень у таблицю tasks
    for _ in range(20):  # Вставляємо 20 випадкових завдань
        title = fake.sentence(nb_words=6)
        description = fake.paragraph(nb_sentences=3)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                    (title, description, status_id, user_id))

    # Збереження змін та закриття з'єднання
    conn.commit()
    cur.close()