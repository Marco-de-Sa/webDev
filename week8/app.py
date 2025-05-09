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

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword:
        return f"Search results for: {keyword}"
    flash('Search keyword cannot be empty!', 'error')
    return render_template('search.html')

@app.route('/submit', methods=['get', 'POST'])
def submit():
    if request.method == 'POST':
        flash('Thank you for submitting!', 'success')
    return render_template('submit.html')


if __name__ == '__main__':
    app.run(debug=True)