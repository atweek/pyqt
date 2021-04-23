import psycopg2

conn = psycopg2.connect(user="ramil",
                              # пароль, который указали при установке PostgreSQL
                              password="ramille",
                              host="127.0.0.1",
                              port="5432")

cur = conn.cursor()
cur.execute("SELECT version();\n")

print(cur.fetchall())
cur.close()