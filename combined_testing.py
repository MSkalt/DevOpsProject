import requests
import pymysql
from pymysql.cursors import DictCursor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Database connection details
db_host = 'sql8.freemysqlhosting.net'
db_user = 'sql8701571'
db_password = 'Hdj2TeCxqg'
db_name = 'sql8701571'
db_port = 3306

# API details
api_url = "http://127.0.0.1:5000/users/1"
user_data = {"user_name": "Max"}

# Selenium setup
chrome_options = Options()
# Comment out the following line to see the browser window
# chrome_options.add_argument("--headless")
service = Service(executable_path="C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
web_url = "http://127.0.0.1:5001"

try:
    # Step 1: Add user via UI
    driver.get(web_url)
    wait = WebDriverWait(driver, 10)
    
    # Find and fill createUser form
    create_form_element = wait.until(EC.presence_of_element_located((By.ID, 'createUserForm')))
    new_user_id_element = create_form_element.find_element(By.NAME, 'new_user_id')
    new_user_name_element = create_form_element.find_element(By.NAME, 'new_user_name')
    
    new_user_id_element.clear()
    new_user_id_element.send_keys("1")
    new_user_name_element.clear()
    new_user_name_element.send_keys("Max")
    create_user_button = create_form_element.find_element(By.XPATH, '//button[@onclick="createUser()"]')
    create_user_button.click()
    
    wait.until(EC.presence_of_element_located((By.ID, 'response')))
    print("User successfully added via UI.")

    # Pause to let the backend process the data
    time.sleep(2)

    # Step 2: Check the user via REST API
    response = requests.get(api_url)
    if response.status_code != 200 or response.json().get("user_name") != "Max":
        raise Exception("Test failed: User not found via API")

    print("User verified via API after creation.")

    # Step 3: Delete user via UI
    delete_form_element = wait.until(EC.presence_of_element_located((By.ID, 'deleteUserForm')))
    delete_user_id_element = delete_form_element.find_element(By.NAME, 'delete_user_id')
    delete_user_id_element.clear()
    delete_user_id_element.send_keys("1")
    delete_user_button = delete_form_element.find_element(By.XPATH, '//button[@onclick="deleteUser()"]')
    delete_user_button.click()
    
    wait.until(EC.presence_of_element_located((By.ID, 'response')))
    print("User successfully deleted via UI.")

    # Pause to let the backend process the data
    time.sleep(2)

    # Step 4: Verify the deletion via REST API
    response = requests.get(api_url)
    if response.status_code != 404:
        raise Exception("Test failed: User still exists via API")

    print("User verified via API after deletion.")

finally:
    driver.quit()
