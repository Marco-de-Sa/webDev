from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret_key'
@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash('Name field cannot be empty!', 'error')
        else:
            return f"Hello, {name}!"
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)