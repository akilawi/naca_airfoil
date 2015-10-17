#from celery import celery
from celery import Celery
from subprocess import call

celery_app = Celery('airfoil_task', backend='amqp', broker='amqp://')

#airfoil command (replace ls with the correct shell command)
AIRFOIL = ""
#path to mesh used as input for airfoil
MESH_PATH = ""


@celery_app.task
def airfoil(num_samples, visc, speed, T, mesh):
    #command = AIRFOIL + ' ' + str(num_samples) + ' ' + str(visc) + ' ' + str(speed) + ' ' + str(T) + ' ' + MESH_PATH + mesh +  ".xml"
    #replace command = 'ls'  with commented line above
    command = 'ls'
    return_code = call(command, shell=True)
    return return_code
