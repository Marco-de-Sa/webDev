from flask import Flask

app = Flask(__name__)
# routes from exercise 1
@app.route('/')
def home():
    return 'Welcome to my website'

@app.route('/about')
def about():
    return 'This is the About page I made with Flask'

if __name__ == '__main__':
    app.run(debug=True)