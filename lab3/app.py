from flask import Flask, render_template, request, flash

from peewee import *
db = SqliteDatabase("patients.db")
class Task(Model):
    title = CharField()
    status = CharField(default="pending")
    class Meta:
        database = db

db.connect()
db.create_tables([Task], safe=True)

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        date = request.form.get('Date')
        NIF = request.form.get('NIF')
        if not name or not email or not date or not NIF:
            flash('All fields are required!', 'error')
        else:
            with open('form_submissions.txt', 'a', encoding='utf-8') as f:
                f.write(f"Name: {name}\nEmail: {email}\nDate: {date}\nNIF: {NIF}\n\n")
            flash('Your form has been submitted!', 'success')
    return render_template('home.html')

@app.route('/list', methods=['GET', 'POST'])
def show_list():
    try:
        with open('form_submissions.txt', 'r', encoding='utf-8') as f:
            submissions = f.read()
    except FileNotFoundError:
        submissions = "No file found please make form_submission.txt first"
    return render_template('list.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)