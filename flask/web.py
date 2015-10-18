from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from subprocess import call
from os import listdir
from os.path import isfile, join
import dolfin_convert


app = Flask(__name__)
app.secret_key = '\x0f\x8bP\x15\xa7\xfb.\xe5\xc0\x13y\x8f>\xc0\x1e(\x99\r\xf1\xe4&\x8d\x8e\xf8'

#Path to run script
RUN_PATH = '../'
#Path to generated meshes that are ready for airfoil
MESHES_PATH = './static/meshes'


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
        #print(arg3)
        command = RUN_PATH + "run.sh " + arg1 + ' ' + arg2 + ' ' + arg3 + ' ' + arg4 + ' ' + arg5
        print(command)
        return_code = call(command, shell=True)
        if return_code != 0:
            #TODO Show some kind of error
            return redirect(url_for('index'))
        meshes = [ f for f in listdir('./msh') if isfile(join('./msh',f)) ]
        for mesh in meshes:
            if "r" + str(arg5) in mesh:
                #print("./dolfin-convert.sh ./msh/" + mesh + " ./static/meshes/" + mesh)
                i = 'msh/' + mesh
                o = 'static/meshes/' + mesh[:-3] + 'xml'
                #dolfin_convert.main(['msh/r0a0n200.msh', 'static/meshes/r0a0n200.xml'])
                dolfin_convert.main([i, o])
                #call("./dolfin-convert.sh ./msh/" + mesh + ". /static/meshes/" + mesh)
        return redirect(url_for('meshes'))
    return redirect(url_for('index'))

@app.route('/meshes')
def meshes():
    #onlyfiles = [ f for f in listdir('./static/meshes') if isfile(join('./static/meshes',f)) ]
    meshes = [ f for f in listdir(MESHES_PATH) if isfile(join(MESHES_PATH,f)) ]
    return render_template('meshes.html', files=meshes)

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
