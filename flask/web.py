from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


app = Flask(__name__)


@app.before_request
def before_request():
    1+1
    #do things that needs to be done before request is processed (connect to database)


@app.teardown_request
def teardown_request(exception):
    1+1
    #do things that needs to be done after a request is processed (close database connection)

@app.route('/')
def index():
    #return send_from_directory('templates', '')
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
