
from subprocess import call
from celery import Celery
import calculations
app = Celery('tasks', backend='rpc://', broker='amqp://')
@app.task
def runMsh(angle , n_nodes , n_levels,speed):
        command='bash runfirst.sh %d %d %d %d %d %d' % (angle , angle , 1 , n_nodes , n_levels , speed)
        print call(command, shell=True)
        return calculations.liftdragratio('navier_stokes_solver/results/%d.m' % angle)







