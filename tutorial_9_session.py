from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "AnyRandomSecretKey"

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('tutorial_9_session_1.html')

@app.route('/login',methods = ['POST'])
def login():
    username = request.form.get('username')
    if not username:
        return redirect(url_for('home'))
    
    session['username'] = username
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    name = session['username']
    return render_template('tutorial_9_session_2.html',name=name)

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)