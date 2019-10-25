from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello_world"


if __name__ == 'main':
    app.run(debug=True)
