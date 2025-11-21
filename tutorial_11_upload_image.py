from flask import Flask, redirect, flash, render_template,request, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = "FlaskUploadImageTutorial"

@app.route('/')
def home():
    return render_template('tutorial_11_file_upload_1.html')

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    error = None
    if request.method == 'POST':
        f = request.files['file']
        if not f or f.filename=="":
            error = "Please upload file"
            return render_template('tutorial_11_file_upload_1.html',error=error)
        f.save(secure_filename(f.filename))
        flash("Your file was uploaded successfully..")
        flash('Your file has been stored and secured')
        username = request.form.get('username')
        return redirect(url_for('upload',username = username))
    return render_template('tutorial_11_file_upload_1.html')

@app.route('/upload/<username>')
def upload(username):
    return render_template('tutorial_11_file_upload_2.html',username=username)

if __name__ == "__main__":
    app.run(debug=True)