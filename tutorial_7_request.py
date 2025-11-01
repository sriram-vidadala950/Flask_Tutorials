from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def DisplayForm():
    return render_template('tutorial_7_request.html')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form['nm']
        mathematics = request.form['maths']
        physics=request.form['phy']
        biology = request.form['bio']
        chemistry = request.form['chy']
        social = request.form['ss']
        return render_template('tutorial_7_request_table.html',name=name,subjects={
            "Mathematics":mathematics,"Physics": physics, "Biology":biology,"Chemisty":chemistry, "Social Studies": social
        })
    else:
        return render_template('tutorial_7_request.html')

if __name__ == "__main__":
    app.run(debug=True)