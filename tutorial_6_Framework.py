from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/user/<name>')
def SayHello(name):
    return render_template("tutorial_6_FW_1.html",name=name)

@app.route('/user/<name>/hello')
def hello(name):
    return render_template("tutorial_6_FW_2.html",name=name)

if __name__ == "__main__":
    app.run(debug=True)