#from celery import celery
from celery import Celery
from subprocess import call

celery_app = Celery('airfoil_task', backend='amqp', broker='amqp://')

#airfoil command (replace ls with the correct shell command)
AIRFOIL_PATH = "../navier_stokes_solver/"
#path to mesh used as input for airfoil
MESH_PATH = "./static/meshes/"


@celery_app.task
def airfoil(num_samples, visc, speed, T, mesh):
    #command = AIRFOIL + ' ' + str(num_samples) + ' ' + str(visc) + ' ' + str(speed) + ' ' + str(T) + ' ' + MESH_PATH + mesh +  ".xml"
    #replace command = 'ls'  with commented line above
    command = AIRFOIL_PATH + 'airfoil ' + str(num_samples) + ' ' + str(visc) + ' ' + str(speed) + ' ' + str(T) + ' ' + MESH_PATH + mesh
    return_code = call(command, shell=True)      #calls the shell command 'command' and returns the return code
    #if return_code == 0:
    command = 'cp results/drag_ligt.m airfoil/' + mesh[:-3] + '.m'
    for i in range(1,100):
        print(command)
    call(command, shell=True)   #replace with function to store result (Using object store?)
    #print('return code: ' + return_code)
    return return_code
