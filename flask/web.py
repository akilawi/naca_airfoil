from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from subprocess import call


app = Flask(__name__)

#Path to run script
RUN_PATH = "./"


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

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        arg1 = request.form['angle_start']
        arg2 = request.form['angle_stop']
        arg3 = request.form['n_angles']
        arg4 = request.form['n_nodes']
        arg5 = request.form['n_levels']
        command = RUN_PATH + "run.sh " + arg1 + ' ' + arg2 + ' ' + arg3 + ' ' + arg4 + ' ' + arg5
        return_code = call(command, shell=True)
        return render_template('index.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
