from flask_app import app
from flask import render_template, redirect, url_for, request
from flask_app.models.users_model import User
# referrence to the app

@app.route("/")
def index():
    return redirect("/users_all")

# ------------- DISPLAY ALL USERS -------------
@app.route('/users_all', methods=['GET'])
def users():
    users = User.get_all()
    return render_template("users_all.html", all_users = users)

# -------------- CREATE USER (render) --------------
@app.route('/users/new')
def new_user():
    return render_template("create_user.html")

# --------------- CREATE USER (action) -----------------
@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        **request.form
    }
    user_id = User.save(data)
    return redirect(url_for('show_user', id = user_id))
# why did URL FOR work for this but not for UPDATE route? Other ways??

# ----------------- DISPLAY ONE USER ------------------
@app.route('/users/show/<int:id>')
def show_user(id):
    user = User.get_one(id)
    return render_template("show_user.html", user = user)

# ------------------- EDIT USER (render) --------------------
@app.route('/users/edit/<int:id>')
def edit_user(id):
    user = User.get_one(id)
    return render_template("edit_user.html", user = user)

# ----------------- EDIT USER (action) -----------------
@app.route('/users/update/<int:id>', methods=["POST"])
def update_user(id):
    data = {
        **request.form,
        "id" : id
    }
    User.edit_user(data)
    return redirect('/')
    # return redirect(url_for('show_user', id = id))

# ------------------- DELETE USER ------------------------
@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')