from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(filename='activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Fungsi untuk mencatat log activity
def log_activity(action, item_type, item_name):
    log_message = f'{action} {item_type}: {item_name}'
    logging.info(log_message)

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman untuk Create User
@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_name = request.form['username']
        # Proses pembuatan user
        # ...
        log_activity('Create', 'User', user_name)
        return 'User created successfully!'
    return render_template('create_user.html')

# Halaman untuk Update User
@app.route('/update-user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_name = request.form['username']
        # Proses update user
        # ...
        log_activity('Update', 'User', user_name)
        return 'User updated successfully!'
    return render_template('update_user.html')

# Halaman untuk Delete User
@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_name = request.form['username']
        # Proses penghapusan user
        # ...
        log_activity('Delete', 'User', user_name)
        return 'User deleted successfully!'
    return render_template('delete_user.html')

# Halaman untuk Create Role
@app.route('/create-role', methods=['GET', 'POST'])
def create_role():
    if request.method == 'POST':
        role_name = request.form['role']
        # Proses pembuatan role
        # ...
        log_activity('Create', 'Role', role_name)
        return 'Role created successfully!'
    return render_template('create_role.html')

# Halaman untuk Update Role
@app.route('/update-role', methods=['GET', 'POST'])
def update_role():
    if request.method == 'POST':
        role_name = request.form['role']
        # Proses update role
        # ...
        log_activity('Update', 'Role', role_name)
        return 'Role updated successfully!'
    return render_template('update_role.html')

# Halaman untuk Delete Role
@app.route('/delete-role', methods=['GET', 'POST'])
def delete_role():
    if request.method == 'POST':
        role_name = request.form['role']
        # Proses penghapusan role
        # ...
        log_activity('Delete', 'Role', role_name)
        return 'Role deleted successfully!'
    return render_template('delete_role.html')

if __name__ == '__main__':
    app.run(debug=True)
