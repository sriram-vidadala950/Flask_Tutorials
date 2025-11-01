from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return f'''
        <h2> Welcome {name}!</h2>
        <a href="/login"> New Response</a>
'''

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for('welcome',name=user))
    else:
        user = request.args.get('nm')
        if user:
            return redirect(url_for('welcome',name=user))
        else:
            return'''
                <form action="/login" method = "POST">
                    <p>Enter Name:</p>
                    <p><input type="text" name="nm"></p>
                    <p><input type="submit" value="Submit"></p>
                </form>
'''


if __name__ == "__main__":
    app.run(debug=True)