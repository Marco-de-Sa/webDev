from flask import Flask, render_template, request, flash, redirect, url_for
from peewee import *
from models import *

db.connect()

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    User.update(login=False).execute()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = User.select().where((User.name == name) & (User.password == password)).first()
        if user:
            user.login = True
            user.save()
            flash('Login successful!')
            return redirect("/welcome")
        else:
            flash('Invalid username or password!')
            # return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    User.update(login=False).execute()
    if request.method == 'POST':
        name = request.form['name']
        login = True
        password = request.form['password']
        is_admin = True if request.form.get('is_admin') == 'on' else False

        if not name or not login or not password:
            flash('All fields are required!')
            return render_template('login.html')

        try:
            user = User.create(name=name, login=login, password=password, is_admin=is_admin)
            flash('User registered successfully!')
        except IntegrityError:
            flash('Login already exists!')

        return render_template('login.html')
    return render_template('register.html')

@app.route('/display')
def display():
    users = User.select()
    students = Student.select()
    classes = Class.select()
    attendances = Attendance.select()
    return render_template('display.html', users=users, students=students, classes=classes, attendances=attendances)

@app.route('/welcome')
def dash_welcome():
    user = User.select().where(User.login == True).first()
    return render_template('dashWelcome.html', user=user)

@app.route('/classes')
def class_manage():
    return render_template('classManage.html')

@app.route('/users')
def user_manage():
    users = User.select()
    students = Student.select()
    current_user = User.select().where(User.login == True).first()
    return render_template('userManage.html', users=users, students=students, current_user=current_user)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone'] or None
        birthdate = request.form['birthdate']
        try:
            Student.create(
                name=name,
                email=email,
                phone=phone,
                birthdate=birthdate
            )
            flash('Student added successfully!')
            return redirect("/users")
        except IntegrityError:
            flash('Email already exists!')
        except Exception as e:
            flash(f'Error: {e}')
    return render_template('addStudent.html')

@app.route('/addTeacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        try:
            User.create(
                name=name,
                password=password,
                is_admin=False,
                login=False
            )
            flash('Teacher added successfully!')
            return redirect("/users")
        except IntegrityError:
            flash('Teacher with this name already exists!')
        except Exception as e:
            flash(f'Error: {e}')
    return render_template('addTeacher.html')

if __name__ == '__main__':
    initialize_db()
    # Set all login fields to False at startup
    User.update(login=False).execute()
    print("Database tables created.")
    app.run(debug=True)