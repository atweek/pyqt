import psycopg2
import keys
class db():
    def __init__(self):
        self.conn = psycopg2.connect(
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
        cursor.execute(f"SELECT pwd FROM users WHERE name = '{name}';")
        pwd = cursor.fetchone()
        cursor.close()
        return pwd
    def logup(self,name, pwd, mobile, email, tg):
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO users (name,pwd,mobile,email,tg) VALUES ('{name}','{pwd}','{mobile}','{email}','{tg}');")
        print ("INSERT 0 1")
        self.conn.commit()
        cursor.close()