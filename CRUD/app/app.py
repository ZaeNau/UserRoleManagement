from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Data
users = []

# Halaman utama
@app.route('/')
def home():
    return render_template('index.html', users=users)

# Halaman tambah user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        role = request.form['role']
        new_user = {"id": len(users) + 1, "username": username, "role": role}
        users.append(new_user)
        return redirect('/')
    return render_template('add_user.html')

# Halaman edit user
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if request.method == 'POST':
        user['username'] = request.form['username']
        user['role'] = request.form['role']
        return redirect('/')
    return render_template('edit_user.html', user=user)

# Halaman hapus user
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    users.remove(user)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
