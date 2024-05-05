import subprocess

def start_app(path):
    return subprocess.Popen(['python', path])

if __name__ == "__main__":
    print("Starting REST API...")
    rest_api = start_app('rest_app.py')

    print("Starting Web Interface...")
    web_app = start_app('web_app.py')

    rest_api.wait()
    web_app.wait()
#comment Master
#comment1
#comment2
#comment3
