import sys
from subprocess import call
from celery import Celery
import calculations
import os

broker_ip = os.environ["BROKER_IP"]
broker_adress = 'amqp://group5:group5@' + broker_ip + ':5672/naca'
app = Celery('tasks', backend='amqp', broker=broker_adress)
#app = Celery('tasks', backend='amqp', broker='amqp://group5:group5@130.238.29.6:5672/naca')
@app.task
def runMsh(angle , n_nodes , n_levels,speed):
        command='bash runfirst.sh %d %d %d %d %d %d' % (angle , angle , 1 , n_nodes , n_levels , speed)
        print call(command, shell=True)
        return calculations.liftdragratio('navier_stokes_solver/results/%d.m' % angle)







