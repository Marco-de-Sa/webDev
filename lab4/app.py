from flask import Flask, render_template, request, flash
import datetime
from peewee import *

db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class FormSubmission(BaseModel):
    name = CharField()
    email = CharField()
    date = CharField()
    nif = CharField()

db.connect()
db.create_tables([FormSubmission], safe=True)

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
            # Save to database instead of file
            FormSubmission.create(name=name, email=email, date=date, nif=NIF)
            flash('Your form has been submitted!', 'success')
    return render_template('home.html')

@app.route('/list', methods=['GET', 'POST'])
def show_list():
    # Fetch all submissions from the database
    submissions = FormSubmission.select()
    return render_template('list.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)