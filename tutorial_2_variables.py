from flask import Flask,request
app = Flask(__name__)
# @app.route('/')
# def hello():
#     return f"Hello,<name>! welcome to the Flask tutorial."

# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']  # get input from form
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''   
if __name__ == "__main__":
    app.run(debug=True)