from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver options
chrome_options = Options()
# Comment out the following line to see the browser window
# chrome_options.add_argument("--headless")

# Path to your ChromeDriver executable
service = Service(executable_path="C:\\chromedriver\\chromedriver.exe")

# Start a WebDriver session
driver = webdriver.Chrome(service=service, options=chrome_options)

# Replace with the root URL of your web app
web_url = "http://127.0.0.1:5001"

try:
    # Visit the specified URL
    driver.get(web_url)
    print(f"Visited URL: {web_url}")

    wait = WebDriverWait(driver, 10)

    try:
        # Create User
        create_form_element = wait.until(EC.presence_of_element_located((By.ID, 'createUserForm')))
        print("Form with id='createUserForm' exists on the page.")
        
        new_user_id_element = create_form_element.find_element(By.NAME, 'new_user_id')
        new_user_name_element = create_form_element.find_element(By.NAME, 'new_user_name')

        # Fill out the form fields to create the user
        new_user_id_element.clear()
        new_user_id_element.send_keys("1")
        new_user_name_element.clear()
        new_user_name_element.send_keys("Max")
        print("Filled out the form fields to create user.")

        # Click the "Create User" button
        create_user_button = create_form_element.find_element(By.XPATH, '//button[@onclick="createUser()"]')
        create_user_button.click()
        print("Clicked the 'Create User' button.")

        # Wait for user creation response
        wait.until(EC.presence_of_element_located((By.ID, 'response')))
        print("User successfully created.")

        # Delete User
        delete_form_element = wait.until(EC.presence_of_element_located((By.ID, 'deleteUserForm')))
        print("Form with id='deleteUserForm' exists on the page.")
        
        delete_user_id_element = delete_form_element.find_element(By.NAME, 'delete_user_id')
        delete_user_id_element.clear()
        delete_user_id_element.send_keys("1")
        
        delete_user_button = delete_form_element.find_element(By.XPATH, '//button[@onclick="deleteUser()"]')
        delete_user_button.click()
        print("Clicked the 'Delete User' button.")

        # Wait for deletion response
        wait.until(EC.presence_of_element_located((By.ID, 'response')))
        print("User successfully deleted.")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    driver.quit()
