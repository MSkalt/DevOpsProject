import subprocess

def start_app(path):
    return subprocess.Popen(['python', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    print("Starting REST API...")
    rest_api = start_app('rest_app.py')

    print("Starting Web Interface...")
    web_app = start_app('web_app.py')

    # Do not wait for these processes to finish, they run in the background
    print("Applications are running in the background.")
