import psycopg2

database = (
    "host=192.168.0.161 dbname='postgres' "
    "user='postgres' password='mysecretpassword'"
)


def create_db():
    with open("task1/scripts.sql", "r") as f:
        sql = f.read()

    with psycopg2.connect(database) as conn:
        cur = conn.cursor()
        cur.execute(sql)


if __name__ == "__main__":
    create_db()
