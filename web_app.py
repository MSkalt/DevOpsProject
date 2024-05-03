from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''
    <html>
        <head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        </head>
        <body>
            <h2>Get User Data</h2>
            <form id="getUserForm">
                Enter User ID: <input type="text" name="user_id">
                <button type="button" onclick="getUser()">Get User</button>
            </form>
            <br>
            <h2>Create User</h2>
            <form id="createUserForm">
                User ID: <input type="text" name="new_user_id">
                User Name: <input type="text" name="new_user_name">
                <button type="button" onclick="createUser()">Create User</button>
            </form>
            <br>
            <h2>Update User</h2>
            <form id="updateUserForm">
                User ID: <input type="text" name="update_user_id">
                New User Name: <input type="text" name="update_user_name">
                <button type="button" onclick="updateUser()">Update User</button>
            </form>
            <br>
            <h2>Delete User</h2>
            <form id="deleteUserForm">
                User ID: <input type="text" name="delete_user_id">
                <button type="button" onclick="deleteUser()">Delete User</button>
            </form>
            <br>
            <div id="response"></div>

            <script>
                function getUser() {
                    var userId = $('[name="user_id"]').val();
                    $.get('http://127.0.0.1:5000/users/' + userId, function(data) {
                        console.log("Get user response: ", data);
                        $('#response').html('<h1>ID: ' + data.user_id + '<br>User: ' + data.user_name + '<br>Created: ' + data.creation_date + '</h1>');
                    }).fail(function(response) {
                        $('#response').html('<h1 id="error">Error: ' + response.responseText + '</h1>');
                    });
                }

                function createUser() {
                    var userId = $('[name="new_user_id"]').val();
                    var userName = $('[name="new_user_name"]').val();
                    $.ajax({
                        url: 'http://127.0.0.1:5000/users/' + userId,
                        type: 'POST',
                        contentType: 'application/json',
                        data: JSON.stringify({ "user_name": userName }),
                        success: function(response) {
                            console.log("Create user response: ", response);
                            $('#response').html('<h1>ID: ' + response.user_id + '<br>User: ' + response.user_name + '<br>Created: ' + response.creation_date + '</h1>');
                        },
                        error: function(response) {
                            $('#response').html('<h1 id="error">Error: ' + response.responseText + '</h1>');
                        }
                    });
                }

                function updateUser() {
                    var userId = $('[name="update_user_id"]').val();
                    var userName = $('[name="update_user_name"]').val();
                    $.ajax({
                        url: 'http://127.0.0.1:5000/users/' + userId,
                        type: 'PUT',
                        contentType: 'application/json',
                        data: JSON.stringify({ "user_name": userName }),
                        success: function(response) {
                            console.log("Update user response: ", response);
                            $('#response').html('<h1>ID: ' + response.user_id + '<br>User: ' + response.user_name + '<br>Created: ' + response.creation_date + '</h1>');
                        },
                        error: function(response) {
                            $('#response').html('<h1 id="error">Error: ' + response.responseText + '</h1>');
                        }
                    });
                }

                function deleteUser() {
                    var userId = $('[name="delete_user_id"]').val();
                    $.ajax({
                        url: 'http://127.0.0.1:5000/users/' + userId,
                        type: 'DELETE',
                        success: function(response) {
                            console.log("Delete user response: ", response);
                            $('#response').html('<h1>ID: ' + response.user_deleted + '<br>User: ' + response.user_name + ' deleted successfully</h1>');
                        },
                        error: function(response) {
                            $('#response').html('<h1 id="error">Error: ' + response.responseText + '</h1>');
                        }
                    });
                }
            </script>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5001)
