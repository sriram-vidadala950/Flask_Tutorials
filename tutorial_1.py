from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask Tutorial</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Flask Tutorial!</h1>
            <p>This is an HTML page served by Flask 🚀</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
