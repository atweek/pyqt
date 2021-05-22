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

    def add_task(self,name,text,date):
        def add(recipient_id,text,date):
            cursor = self.conn.cursor()
            print(date)
            date_dst = date[19:30]
            try:
                cursor.execute(f"INSERT INTO tasks (text,owner_id,recipient_id,deadline)"
                           f"VALUES ('{text}','{self.id}','{recipient_id[0]}','{date_dst}');")
                print("INSERT 0 1")
            except TypeError:
                return 0
            self.conn.commit()
            cursor.close()
            return 1

        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT id FROM users WHERE name = '{name}';")
        except TypeError:
            return 0
        recipient_id = cursor.fetchone()
        cursor.close()
        return add(recipient_id,text,date)

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
    def get_name(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM users WHERE id = '{self.id}';")
        return cursor.fetchone()[0]
        cursor.close()
    def count_task(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM tasks WHERE recipient_id = {self.id};")
        ret = cursor.fetchone()[0]
        cursor.close()
        return ret
    def count_events(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM events;")
        ret = cursor.fetchone()[0]
        cursor.close()
        return ret
    def check_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT text,users.name,tasks.id,tasks.deadline FROM tasks "
                       f"INNER JOIN users ON users.id = tasks.owner_id WHERE recipient_id = {self.id};")
        ret = cursor.fetchall()
        cursor.close()
        return ret
    def del_task(self,id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE id = {int(id)}")
        self.conn.commit()
        cursor.close()
    def check_events(self):
        def clean_old():
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM events WHERE time < date(now())")
            self.conn.commit()
            cursor.close()
        def get_events():
            cursor = self.conn.cursor()
            cursor.execute("SELECT name,disc,place,time,length FROM events  WHERE time > NOW() ORDER BY time;")
            ret = cursor.fetchall()
            cursor.close()
            return ret
        clean_old()
        # self.count = count_events()
        # print(f"count = {self.count}\n")
        info = get_events()
        # print(info)
        return info
    # def add_task(self):

