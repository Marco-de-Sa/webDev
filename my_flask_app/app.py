from flask import Flask, render_template

app = Flask(__name__)
# routes from exercise 1
@app.route('/')
def home():
    return 'Welcome to my website'

@app.route('/about')
def about():
    return 'This is the About page I made with Flask'

@app.route('/contact')
def contact():
    return 'Contact me at: example@gmail.com'

@app.route('/profile/<name>')
def profile(name):
    age = 25 # Example static data
    hobby = "Reading" # Example static data
    return render_template('profile.html', name=name, age=age, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)