import psycopg2
import keys

conn = psycopg2.connect(
     dbname=keys.dbname,
     user=keys.db_user,
     password=keys.dbpwd,
     host=keys.dbhost,
     port=keys.dbport)
cur = conn.cursor()
cur.execute("SELECT version();\n")
print(cur.fetchall())
cur.close()

def bot_cheak_user(name):
    global user_id
    cursor = conn.cursor()
    cursor.execute(f"SELECT id,tg_id FROM users WHERE tg = '{name}';")
    tg_id = cursor.fetchone()
    cursor.close()
    if tg_id[1] == None:
        return -1
    else:
        return tg_id
def logup(name,id):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET tg_id = {id} WHERE tg = '{name}'")
    conn.commit()
    cursor.close()
def event_len():
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM events")
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret

def event(i):
    cursor = conn.cursor()
    cursor.execute(f"SELECT name, disc, place, time FROM events ")
    info = cursor.fetchall()
    cursor.close()
    time = str(info[i][3])
    # time1 = str(time)
    t = f"{info[i][0]}\n{info[i][1]}\n{info[i][2]}\n{time[0:19]}"
    return t
def task_len(user_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM tasks WHERE recipient_id = '{user_id}'")
    ret = cursor.fetchone()[0]
    cursor.close()
    print(ret)
    print("\n" + str(user_id))
    return ret
def get_id(name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM users WHERE tg = '{name}'")
    info = cursor.fetchone()[0]
    cursor.close()
    return info

def get_name(user_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM users WHERE id = '{user_id}'")
    info = cursor.fetchone()[0]
    cursor.close()
    return info

def task(i,user_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT text, deadline,owner_id FROM tasks WHERE recipient_id = '{user_id}'")
    info = cursor.fetchall()
    cursor.close()
    time = str(info)
    # time1 = str(time)
    t = f"{info[i][0]}\n{info[i][1]}\n{get_name(info[i][2])}\n"
    print(t)
    return t
def contact(name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT tg FROM users WHERE name = '{name}'")
    info = cursor.fetchall()
    cursor.close()
    try:
        return info[0]
    except:
        return -1

def change(pwd,name):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET pwd = '{pwd}' WHERE tg = '{name}';")
    conn.commit()
    cursor.close()