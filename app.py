from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world() -> object:  # put application's code here
# return '<h1> Hello World! <h1>'

@app.route('/')
def index() -> object:
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
