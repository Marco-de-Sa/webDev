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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile/<name>')
def profile(name):
    age = 25 # Example static data
    hobby = "Reading" # Example static data
    return render_template('profile.html', name=name, age=age, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)