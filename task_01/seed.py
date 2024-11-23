from connect import create_connection

from faker import Faker
import random

with create_connection() as conn:
    cur = conn.cursor()

    fake = Faker()

    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", (status,))

    for _ in range(10):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (fullname, email))

    cur.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cur.fetchall()]

    for _ in range(20):
        title = fake.sentence(nb_words=6)
        description = fake.paragraph(nb_sentences=3)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                    (title, description, status_id, user_id))

    conn.commit()
    cur.close()