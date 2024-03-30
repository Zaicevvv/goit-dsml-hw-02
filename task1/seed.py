import psycopg2
import faker
from random import randint, choice
from main import database


def generate_fake_data():
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(10):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(10):
        fake_tasks.append((fake_data.sentence(), fake_data.text()))

    return fake_users, fake_tasks


def prepare_data(users, tasks):
    for_users = []
    for user in users:
        for_users.append((*user,))

    for_status = []
    for i in range(3):
        values = ["new", "in progress", "completed"]
        for_status.append((values[i],))

    for_tasks = []
    for task in tasks:
        for_tasks.append((*task, randint(1, 3), randint(1, 10)))

    return for_users, for_status, for_tasks


def insert_data_to_db(users, status, tasks):
    with psycopg2.connect(database) as conn:
        try:
            cur = conn.cursor()

            sql_to_users = """
                INSERT INTO users (fullname, email) VALUES (%s,%s);
            """
            cur.executemany(sql_to_users, users)

            sql_to_status = """
                INSERT INTO status (name) VALUES (%s);
            """
            cur.executemany(sql_to_status, status)

            sql_to_tasks = """
                INSERT INTO tasks (title, description, status_id, user_id)
                VALUES (%s,%s,%s,%s);
            """
            cur.executemany(sql_to_tasks, tasks)

            conn.commit()
        except psycopg2.Error as e:
            print("[ERROR] An error occurred:", e)


if __name__ == "__main__":
    users, status, tasks = prepare_data(*generate_fake_data())
    insert_data_to_db(users, status, tasks)
