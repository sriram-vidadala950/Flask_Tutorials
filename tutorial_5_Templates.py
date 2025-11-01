from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/user/<name>')
def welcome(name):
    html = f'''
    <html>
        <body>
            <p>Hello {name}</p>
            <a href="/">New Response</a>
        </body>
    </html>
    '''
    return html

@app.route('/login', methods=['POST'])
def login():
    name = request.form['nm']
    if not name:
        return redirect(url_for("index"))  # prevent /user/ empty redirect
    return redirect(url_for("welcome", name=name))

@app.route('/')
def index():
    return render_template('tutorial_3_HTTP.html')

if __name__ == "__main__":
    app.run(debug=True)
