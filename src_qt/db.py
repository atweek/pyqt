import psycopg2
import keys
import random
class db():
    def __init__(self):
        self.conn = psycopg2.connect(
                                dbname=keys.dbname,
                                user=keys.db_user,
                                password=keys.dbpwd,
                                host=keys.dbhost,
                                port=keys.dbport)
        cur = self.conn.cursor()
        cur.execute("SELECT version();\n")
        print(cur.fetchall())
        cur.close()
    def chaeck_pwd(self,name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT pwd,id FROM users WHERE name = '{name}';")
        info = cursor.fetchone()
        # print(info)
        self.id = info[1]
        pwd = info[0]
        cursor.close()
        return pwd
    def get_av(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT avatar FROM users WHERE id = '{self.id}';")
        av = cursor.fetchone()
        cursor.close()
        return av[0]
    def logup(self,name, pwd, mobile, email, tg):
        av = "av" + str(random.randrange(1, 6, 1))
        print(av + "\n")
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO users (name,pwd,mobile,email,tg,avatar)"
                       f"VALUES ('{name}','{pwd}','{mobile}','{email}','{tg}', '{av}');")
        print ("INSERT 0 1")
        self.conn.commit()
        cursor.close()