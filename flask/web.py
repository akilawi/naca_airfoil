from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from subprocess import call
from os import listdir
from os.path import isfile, join
import dolfin_convert
import airfoil_task

import sys
sys.path.insert(0, '../')
import run 

#import the module responsible to add tasks to the queue

app = Flask(__name__)
app.secret_key = '\x0f\x8bP\x15\xa7\xfb.\xe5\xc0\x13y\x8f>\xc0\x1e(\x99\r\xf1\xe4&\x8d\x8e\xf8'

#Path to run script
RUN_PATH = '../'
#Path to generated meshes that are ready for airfoil
MESHES_PATH = '../msh'

 
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

@app.route('/generation')
def generation():
    #return send_from_directory('templates', '')
    return render_template('generation.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        arg1 = request.form['angle_start']
        arg2 = request.form['angle_stop']
        arg3 = request.form['n_angles']
        arg4 = request.form['n_nodes']
        arg5 = request.form['n_levels']
        arg6 = request.form['speed']
        #print(arg3)
        run.splitTasks(int(arg1),int(arg2),int(arg3),int(arg4),int(arg5),int(arg6))
        return_code=1
        # command = RUN_PATH + "run.sh " + arg1 + ' ' + arg2 + ' ' + arg3 + ' ' + arg4 + ' ' + arg5
        # print(command)
        # return_code = call(command, shell=True)
        if return_code != 0:
            #TODO Show some kind of error
            return redirect(url_for('index'))
        return redirect(url_for('meshes'))
    return redirect(url_for('index'))

@app.route('/meshes')
def meshes():
    #onlyfiles = [ f for f in listdir('./static/meshes') if isfile(join('./static/meshes',f)) ]
    meshes = [ f for f in listdir(MESHES_PATH) if isfile(join(MESHES_PATH,f)) ]
    return render_template('meshes.html', files=meshes)

@app.route('/airfoil', methods=['POST', 'GET'])
def airfoil():
    if request.method == 'POST':
        meshes = [ f for f in listdir('./static/meshes') if isfile(join('./static/meshes',f)) ]
        for mesh in meshes:
            TASK_QUEUE.append(airfoil_task.airfoil.delay(10, 0.001, 10.0, 1.0, mesh))
    return render_template('airfoil.html')

@app.route('/status')
def status():
    tasks = []
    for t in run.TASK_QUEUE:
        if(t.ready()):
            tasks.append('Task not yet complete')
        else:
            tasks.append('Task complete')
    return render_template('status.html', tasks=tasks)

#@app.route('/generating/<listOfObjects>')
#def generating_meshes(listOfObjects):
    #if request.method == 'POST':
    #    arg1 = request.form['angle_start']
    #    arg2 = request.form['angle_stop']
    #    arg3 = request.form['n_angles']
    #    arg4 = request.form['n_nodes']
    #    arg5 = request.form['n_levels']
    #    arg6 = request.form['speed']
    #    arg7 = request.form['n_vm']
        #print(arg3)
        ##command = RUN_PATH + "run.sh " + arg1 + ' ' + arg2 + ' ' + arg3 + ' ' + arg4 + ' ' + arg5
    #    print(command)
    #    return_code = call(command, shell=True)
    #    return redirect(url_for('index'))
    #return render_template('generating.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
