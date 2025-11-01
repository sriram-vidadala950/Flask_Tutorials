from flask import Flask, request, url_for, render_template, make_response, redirect

app = Flask(__name__)

@app.route("/")
def login_form():
    return render_template('tutorial_8_cookies_1.html')

@app.route("/login", methods=["POST","GET"])
def get_cookies():
    if request.method == "POST":
        user = request.form.get('uname','none')
        resp = make_response(redirect(url_for('stage1')))
        resp.set_cookie('username',user,max_age=3*60)
        return resp
    else:
        return render_template('tutorial_8_cookies_1.html')


@app.route("/stage1", methods=["POST","GET"])
def stage1():
    user = request.cookies.get("username")
    if not user:
        return redirect(url_for("login_form"))
    if request.method == "POST":
        company = request.form.get("company","none")
        role = request.form.get("role","none")
        resp = make_response(redirect(url_for("stage3")))
        resp.set_cookie('company', company, max_age=60)
        resp.set_cookie('role', role, max_age=60)
        return resp
    return render_template('tutorial_8_cookies_3.html')


@app.route('/stage3', methods=['POST','GET'])
def stage3():
    user = request.cookies.get('username')
    company = request.cookies.get('company')
    role = request.cookies.get('role')
    if not user or not company or not role:
        return redirect(url_for('login_form'))
    if request.method == "POST":
        character = request.form.get('character')
        resp = make_response(redirect(url_for('welcome')))
        resp.set_cookie('character',character,max_age=3*60)
        return resp
    return render_template('tutorial_8_cookies_4.html')
@app.route("/welcome")
def welcome():
    user = request.cookies.get("username")
    company = request.cookies.get("company")
    role = request.cookies.get('role')
    character = request.cookies.get('character')
    if user and company and role and character:
        return render_template('tutorial_8_cookies_2.html',name=user, company=company, role=role, character=character)
    else:
        return redirect(url_for("login_form"))
    

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for('login_form')))
    resp.set_cookie('username','',expires=0)
    resp.set_cookie('company','',expires=0)
    resp.set_cookie('role','',expires=0)
    resp.set_cookie('character','',expires=0)
    return resp

if __name__ == "__main__":
    app.run(debug=True)