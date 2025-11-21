from flask import Flask, redirect, url_for, render_template, flash, request
app = Flask(__name__)

app.route('/')
def home():
    return render_template('tutorial_10_flash_message_2.html')

app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.get == 'POST':
        if request.form['username'] !='admin' or request.form['password'] !='admin@123':
            error = "Invalid Username or Password"
        else:
            flash("You were successfully logged in..")
            flash('Logout before login again..')
            return redirect(url_for('home'))