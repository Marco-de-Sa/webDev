from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret_key'
# routes from exercise 1
@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash('Name field cannot be empty!', 'error')
        else:
            return f"Hello, {name}!"
    return render_template('greet.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if not name or not message:
            flash('All fields are required!', 'error')
        else:
            with open('contact_submissions.txt', 'a', encoding='utf-8') as f:
                f.write(f"Name: {name}\nMessage: {message}\n---\n")
            flash('Your message has been submitted!', 'success')
    return render_template('contact.html')

@app.route('/profile/<name>')
def profile(name):
    age = 25 # Example static data
    hobby = "Reading" # Example static data
    return render_template('profile.html', name=name, age=age, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)