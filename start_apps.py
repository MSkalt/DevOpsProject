import subprocess

def start_app(command):
    return subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    print("Starting REST API...")
    rest_api = start_app('python rest_app.py')

    print("Starting Web Interface...")
    web_app = start_app('python web_app.py')

    print("Applications are running in the background.")
