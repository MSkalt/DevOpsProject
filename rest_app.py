
"""
This module contains the REST API implementation using Flask.

Functions:
- create_user(user_id): Creates a user with the given ID.
- read_user(user_id): Reads user data with the given ID.
- update_user_route(user_id): Updates the user data.
- delete_user_route(user_id): Deletes the user data.
"""



from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connector import add_user, get_user, update_user, delete_user
import logging
import os
import signal

# Configure basic logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

@app.route('/users/<int:user_id>', methods=['POST'])
def create_user(user_id):
    try:
        data = request.get_json()
        if not data or 'user_name' not in data:
            logging.error("Missing 'user_name' in request data")
            return jsonify(status='error', reason='missing parameter "user_name"'), 400

        if add_user(user_id, data['user_name']):
            user = get_user(user_id)
            return jsonify(
                status='ok',
                user_id=user['user_id'],
                user_name=user['user_name'],
                creation_date=user['creation_date']
            ), 200
        else:
            return jsonify(status='error', reason='id already exists'), 409
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        return jsonify(status='error', reason=str(e)), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    try:
        user = get_user(user_id)
        if user:
            return jsonify(
                status='ok',
                user_id=user['user_id'],
                user_name=user['user_name'],
                creation_date=user['creation_date']
            ), 200
        else:
            return jsonify(status='error', reason='no such id'), 404
    except Exception as e:
        logging.error(f"Error reading user: {e}")
        return jsonify(status='error', reason=str(e)), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    try:
        data = request.get_json()
        if not data or 'user_name' not in data:
            logging.error("Missing 'user_name' in request data")
            return jsonify(status='error', reason='missing parameter "user_name"'), 400

        if update_user(user_id, data['user_name']):
            user = get_user(user_id)
            return jsonify(
                status='ok',
                user_id=user['user_id'],
                user_name=user['user_name'],
                creation_date=user['creation_date']
            ), 200
        else:
            return jsonify(status='error', reason='no such id'), 404
    except Exception as e:
        logging.error(f"Error updating user: {e}")
        return jsonify(status='error', reason=str(e)), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    try:
        user = get_user(user_id)
        if user and delete_user(user_id):
            return jsonify(
                status='ok',
                user_deleted=user_id,
                user_name=user['user_name']
            ), 200
        else:
            return jsonify(status='error', reason='no such id'), 404
    except Exception as e:
        logging.error(f"Error deleting user: {e}")
        return jsonify(status='error', reason=str(e)), 500

if __name__ == '__main__':
    # Bind to all interfaces on the host
    app.run(debug=True, host='0.0.0.0', port=5000)
