from flask import Flask, render_template

app = Flask(__name__)
# routes from exercise 1
@app.route('/')
def home():
    return render_template('home.html')

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