import pymysql
from pymysql.cursors import DictCursor

def connect_db():
    return pymysql.connect(host='sql8.freemysqlhosting.net',
                           user='sql8701571',
                           password='Hdj2TeCxqg',
                           db='sql8701571',
                           port=3306,
                           charset='utf8mb4',
                           cursorclass=DictCursor)




def get_user(user_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            return result
    finally:
        conn.close()

def add_user(user_id, user_name):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, NOW())"
            cursor.execute(sql, (user_id, user_name))
            conn.commit()
            return cursor.rowcount == 1
    except pymysql.err.IntegrityError:
        return False
    finally:
        conn.close()

def update_user(user_id, user_name):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE users SET user_name = %s WHERE user_id = %s"
            cursor.execute(sql, (user_name, user_id))
            conn.commit()
            return cursor.rowcount == 1
    finally:
        conn.close()

def delete_user(user_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            conn.commit()
            return cursor.rowcount == 1
    finally:
        conn.close()
