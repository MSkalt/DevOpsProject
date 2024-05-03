import requests
import pymysql
from pymysql.cursors import DictCursor

# Database connection details
db_host = 'sql8.freemysqlhosting.net'
db_user = 'sql8701571'
db_password = 'Hdj2TeCxqg'
db_name = 'sql8701571'
db_port = 3306

# API details
api_url = "http://127.0.0.1:5000/users/1"
user_data = {"user_name": "Max"}

# Step 1: POST new user data
response = requests.post(api_url, json=user_data)
if response.status_code != 200:
    raise Exception("test failed: POST request failed")

print(f"User '{user_data['user_name']}' successfully created via POST.")

# Step 2: Check the data in the database to ensure it was created
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, port=db_port, cursorclass=DictCursor)
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_name FROM users WHERE user_id = 1")
        db_user_data = cursor.fetchone()
        if not db_user_data or db_user_data["user_name"] != user_data["user_name"]:
            raise Exception("test failed: Database data mismatch")
finally:
    connection.close()

print("User data matches the data in the database.")

# Step 3: DELETE the user
response = requests.delete(api_url)
if response.status_code != 200:
    raise Exception("test failed: DELETE request failed")

print(f"User '{user_data['user_name']}' successfully deleted via DELETE.")

# Step 4: Verify the user was deleted from the database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, port=db_port, cursorclass=DictCursor)
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_name FROM users WHERE user_id = 1")
        db_user_data = cursor.fetchone()
        if db_user_data:
            raise Exception("test failed: User still exists in the database after deletion")
finally:
    connection.close()

print("User successfully removed from the database.")
