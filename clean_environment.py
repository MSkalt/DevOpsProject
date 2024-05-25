import requests

try:
    # Attempt to stop the REST API server
    response = requests.get('http://127.0.0.1:5000/stop_server')
    if response.status_code == 200:
        print("REST API server stopped.")
    else:
        print(f"Failed to stop REST API server: {response.text}")
except Exception as e:
    print(f"Error stopping REST API server: {str(e)}")

try:
    # Attempt to stop the Web App server
    response = requests.get('http://127.0.0.1:5001/stop_server')
    if response.status_code == 200:
        print("Web App server stopped.")
    else:
        print(f"Failed to stop Web App server: {response.text}")
except Exception as e:
    print(f"Error stopping Web App server: {str(e)}")
