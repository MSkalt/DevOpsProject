import subprocess
import os

def start_app(path):
    process = subprocess.Popen(['python', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line.decode().strip())
    for line in process.stderr:
        print(line.decode().strip())
    return process

if __name__ == "__main__":
    if not os.path.exists('rest_app.py') or not os.path.exists('web_app.py'):
        print("One or more application files do not exist")
    else:
        print("Starting REST API...")
        rest_api = start_app('rest_app.py')

        print("Starting Web Interface...")
        web_app = start_app('web_app.py')

        print("Applications are running in the background.")
